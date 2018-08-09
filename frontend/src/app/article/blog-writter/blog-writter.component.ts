import { Component, OnInit } from '@angular/core';
import { GlobalVars } from '../../app.component';
import { LoginCheckerService } from '../../_helpers/login-checker.service';
import { IArticle, CArticle } from '../../_interfaces/article-interface.article';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../_services/api.service';

@Component({
  selector: 'app-blog-writter',
  templateUrl: './blog-writter.component.html',
  styleUrls: ['./blog-writter.component.css']
})

export class BlogWritterComponent implements OnInit {

  article = {};
  categories = [];
  sub_categories = [];
  editorContent = '';
  article_title = ''; 

  public options: Object = {
    placeholderText: 'Edit Your Content Here!',
    charCounterCount: false,
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
  ) {
    _gvars.context = 'writer';
    // tslint:disable-next-line:no-debugger
    if (_loginChecker.is_loggedin()) {
      _gvars.isLoggedIn = true;
    }
  }

  ngOnInit() {
    localStorage.setItem('context', 'writer');
    this.get_cat();
  }

  get_cat() {
    this._ApiService.getCategories().subscribe(data => {
      this.categories = data['objects'];
    });
  }

  fetchSuvctgry(cat) {
    console.log(cat);
    this._ApiService.getSubCategories(cat).subscribe(data => {
      // tslint:disable-next-line:no-debugger
      debugger;
      this.sub_categories = data['objects'];
    });
  }

  save() {
    // tslint:disable-next-line:no-debugger
    debugger;
    this.article['article_content'] = this.editorContent;
    this.article['author'] = JSON.parse(localStorage.getItem('user_resource')).resource_uri;
    this._ApiService.saveArticle(this.article).subscribe(data => {
      console.log(data);
    });
  }
}
