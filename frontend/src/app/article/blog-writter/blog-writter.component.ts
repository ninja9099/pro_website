import { Component, OnInit, ViewContainerRef } from '@angular/core';
import { GlobalVars } from '../../app.component';
import { LoginCheckerService } from '../../_helpers/login-checker.service';

import { ApiService } from '../../_services/api.service';
import { ToastsManager } from 'ng2-toastr';
import { CArticle } from '../../_interfaces/article-interface.article';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-blog-writter',
  templateUrl: './blog-writter.component.html',
  styleUrls: ['./blog-writter.component.css']
})

export class BlogWritterComponent implements OnInit {

  categories = [];
  sub_categories = [];
  data = [];
  image: any;
  has_catError = false;
  hasSubcatError = false;
  public article: CArticle;
  public _params: object;

  constructor(public _gvars: GlobalVars,
    public _loginChecker: LoginCheckerService,
    private _ApiService: ApiService,
    public vcr: ViewContainerRef,
    public toastr: ToastsManager,
    private route: ActivatedRoute
  ) {
    _gvars.context = 'writer';
    if (_loginChecker.is_loggedin()) {
      _gvars.isLoggedIn = true;
    }
    this.toastr.setRootViewContainerRef(vcr);
    this.route.params.subscribe(params => this._params = params);
  }

  public options: Object = {
    placeholder: 'Edit Me',
    imageUploadURL: 'http://localhost:8000/api/v1/editor/image/',
    events: {
      'froalaEditor.contentChanged': function (e, editor) {
        console.log(editor.selection.get());
      }
    },
    height: 450
  };
  ngOnInit() {
    localStorage.setItem('context', 'writer');
    this.get_cat();
    const isDrfatPresent = localStorage.getItem('article');
    if (isDrfatPresent) {
      const do_confirm = confirm('do you want to continue edit of draft');
      if (do_confirm) {
        this.article = Object.assign({}, JSON.parse(isDrfatPresent));
        localStorage.removeItem('article');
      }
    } else if (this._params.hasOwnProperty('edit')) {
      // tslint:disable-next-line:no-debugger
      debugger;
        if (this._params.hasOwnProperty('article')) {
          const edit_id = this._params['article'];
          // tslint:disable-next-line:no-debugger
          debugger;
          this._ApiService.getArticle(edit_id).subscribe(data => {
            this.fetchSubctgry(data['article_category'] );
            this.article = Object.assign({}, data); });

        }
    } else {
      this.article = new CArticle({
        article_content: null,
        article_image: null,
        article_tags: null,
        article_title: null,
        article_category: 'default',
        article_subcategory: 'default',
        article_id: null,
      });
    }
  }
  get_cat() {
    this._ApiService.getCategories().subscribe(data => {
      for (const key in data) {
        if (data.hasOwnProperty(key)) {
          this.categories.push(data[key]);
        }
      }
    });
  }

  validateCategory(value) {
    if (value === 'default') {
      this.has_catError = true;
      return;
    } else {
      this.has_catError = false;
    }
  }

  validateSubCategory (value) {
    if (value === 'default') {
      this.hasSubcatError = true;
      return ;
    } else {
      this.hasSubcatError = false;
    }
  }
  onFileChange(event) {
    // tslint:disable-next-line:no-debugger
    const reader = new FileReader();
    if (event.target.files && event.target.files.length > 0) {
      const file = event.target.files[0];
      reader.readAsDataURL(file);
      reader.onload = () => {
        this.image = reader.result;
      };
    }
  }

  fetchSubctgry(cat, params={}) {
    if (cat !== 'default') {
      this._ApiService.getSubCategories(cat, params).subscribe(data => {
        for (const key in data) {
          if (data.hasOwnProperty(key)) {
          this.sub_categories.push(data[key]);
          }
        }
      });
    }
  }
  public preSave() {
    const article_to_send = Object.assign({}, this.article);
    article_to_send.article_image = this.image;
    article_to_send.article_author = JSON.parse(localStorage.getItem('user_id'));
    return JSON.stringify(article_to_send);
  }

  draft () {
    localStorage.setItem('article', JSON.stringify(this.article));
  }

  updateArticle(updatedArticle, id) {
    this._ApiService.updateArticle(updatedArticle, id).subscribe(data => {
      this.toastr.success('saved!', 'Success!');
    },
      error => {
        this.toastr.success(error, 'Error!');
  });
  }

  save() {
    if (this.article.article_id) {
      const saved_article = this.preSave();
      this.updateArticle(saved_article, this.article.article_id);
      return;
    }
    const article = this.preSave();
    this._ApiService.saveArticle(article).subscribe(data => {
      console.log(data);
      this.toastr.success('You are awesome!', 'Success!');
      if ('id' in data) {
        this.article.article_id = data.id;
      }
    },
    error => {
      this.toastr.error(JSON.stringify(error.error), 'Error!');
    });
  }
}
