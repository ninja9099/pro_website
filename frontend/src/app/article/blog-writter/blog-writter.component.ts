import { Component, OnInit, ViewContainerRef } from '@angular/core';
import { GlobalVars } from '../../app.component';
import { LoginCheckerService } from '../../_helpers/login-checker.service';

import { ApiService } from '../../_services/api.service';
import { ToastsManager } from 'ng2-toastr';
import { CArticle } from '../../_interfaces/article-interface.article';

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

  constructor(public _gvars: GlobalVars,
    public _loginChecker: LoginCheckerService,
    private _ApiService: ApiService,
    public vcr: ViewContainerRef,
    public toastr: ToastsManager,
  ) {
    _gvars.context = 'writer';
    if (_loginChecker.is_loggedin()) {
      _gvars.isLoggedIn = true;
    }
    this.toastr.setRootViewContainerRef(vcr);
  }

  public options: Object = {
    placeholder: "Edit Me",
    events: {
      'froalaEditor.contentChanged': function (e, editor) {
        console.log(editor.selection.get());
      }
    }
  }
  ngOnInit() {
    localStorage.setItem('context', 'writer');
    this.get_cat();
    let isDrfatPresent = localStorage.getItem('article');
    if (isDrfatPresent) {
      let do_confirm = confirm('do you want to continue edit of draft');
      if (do_confirm){
      this.article = Object.assign({}, JSON.parse(isDrfatPresent));
      localStorage.removeItem('article');
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
    let reader = new FileReader();
    if (event.target.files && event.target.files.length > 0) {
      let file = event.target.files[0];
      reader.readAsDataURL(file);
      reader.onload = () => {
        this.image = reader.result;
      };
    }
  }

  fetchSubctgry(cat) {
    if (cat !== 'default') {
      this._ApiService.getSubCategories(cat).subscribe(data => {
        for (const key in data) {
          if (data.hasOwnProperty(key)) {
          this.sub_categories.push(data[key]);
          }
        }
      });
    }
  }
  public preSave() {
    let article_to_send = Object.assign({}, this.article);
    article_to_send.article_image = this.image;
    article_to_send.article_author = JSON.parse(localStorage.getItem('user_id'));
    return JSON.stringify(article_to_send);
  }

  draft () {
    localStorage.setItem('article', JSON.stringify(this.article));
  }

  updateArticle(id) {
    this._ApiService.updateArticle(this.article, id).subscribe(data => {
      // tslint:disable-next-line:no-debugger
      debugger;
      this.toastr.success('saved!', 'Success!');
    });
  }


  save() {
    if (this.article.article_id) {
      this.updateArticle(this.article.article_id);
      return;
    }
    let article = this.preSave();
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
