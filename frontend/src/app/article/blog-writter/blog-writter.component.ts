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
  public article: CArticle;
  data = [];
  image: any;
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

  ngOnInit() {
    localStorage.setItem('context', 'writer');
    this.get_cat();

    this.article = new CArticle({
      article_content : null,
      article_image : null,
      article_tags: null,
      article_title: null,
      article_category: null,
      article_subcategory: null, });
  }
  get_cat() {
    this._ApiService.getCategories().subscribe(data => {
      for (const key in data) {
        if (data.hasOwnProperty(key)){
          this.categories.push(data[key]);

        }
      }
    });
  }

  onFileChange(event) {
    // tslint:disable-next-line:no-debugger
    debugger;
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
    this._ApiService.getSubCategories(cat).subscribe(data => {
      for (const key in data) {
        if (data.hasOwnProperty(key)) {
        this.sub_categories.push(data[key]);
        }
      }
    });
  }

  public preSave() {
    let article_to_send = Object.assign({}, this.article);
    article_to_send.article_image = this.image;
    article_to_send.article_author = JSON.parse(localStorage.getItem('user_id'));
    return JSON.stringify(article_to_send);
  }


  save() {
    let article = this.preSave();
    // tslint:disable-next-line:no-debugger
    debugger;
    this._ApiService.saveArticle(article).subscribe(data => {
      console.log(data);
      this.toastr.success('You are awesome!', 'Success!');
    },
    error => {
      this.toastr.error(JSON.stringify(error.error), 'Error!');
    });
  }
}
