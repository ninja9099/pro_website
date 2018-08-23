import { Component, OnInit, ViewContainerRef } from '@angular/core';
import { GlobalVars } from '../../app.component';
import { LoginCheckerService } from '../../_helpers/login-checker.service';

import { FormsModule, FormBuilder, Validators, FormGroup } from '@angular/forms';
import { ApiService } from '../../_services/api.service';
import { ToastsManager } from 'ng2-toastr';

@Component({
  selector: 'app-blog-writter',
  templateUrl: './blog-writter.component.html',
  styleUrls: ['./blog-writter.component.css']
})

export class BlogWritterComponent implements OnInit {

  article = {};
  categories = {};
  sub_categories = {};
  article_image;
  tags = [];

  public options: Object = {
    placeholderText: 'Edit Your Content Here!',
    charCounterCount: false,
    minHeight: 500,
    events: {
      'froalaEditor.focus': function (e, editor) {
        console.log(editor.selection.get());

      },
      'froalaEditor.contentChanged': function(e, editor) {
        console.log(e.editorContent);
        console.log(editor);
      }
    }
  };

  constructor(public _gvars: GlobalVars,
    public _loginChecker: LoginCheckerService,
    private _ApiService: ApiService,
    public vcr: ViewContainerRef,
    public toastr: ToastsManager,
  ) {
    _gvars.context = 'writer';
    // tslint:disable-next-line:no-debugger
    if (_loginChecker.is_loggedin()) {
      _gvars.isLoggedIn = true;
    }
    this.toastr.setRootViewContainerRef(vcr);
  }

  ngOnInit() {
    localStorage.setItem('context', 'writer');
    this.get_cat();
  }

  get_cat() {
    this._ApiService.getCategories().subscribe(data => {
      this.categories = data;
    });
  }

  fetchSubctgry(cat) {

    this._ApiService.getSubCategories(cat).subscribe(data => {
      this.sub_categories = data
    });
  }

  save() {
    this.tags.forEach(element => {
      // tslint:disable-next-line:no-debugger
      this.tags.push({
        'name': element.display,
        'slug': element.value,
        'fake_field': element.value, });
    });
    this.article['article_tags'] = this.tags;
    this.article['article_author'] = JSON.parse(localStorage.getItem('user_id'));
    // this.article['article_image'] = this.article.article_image;
    this._ApiService.saveArticle(JSON.stringify(this.article)).subscribe(data => {
      console.log(data);
      this.toastr.success('You are awesome!', 'Success!');
    },
    error => {
      this.toastr.error(JSON.stringify(error.error), 'Error!');
    });
  }
}
