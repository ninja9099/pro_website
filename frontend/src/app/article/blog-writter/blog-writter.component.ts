import { Component, OnInit } from '@angular/core';
import { GlobalVars } from '../../app.component';
import { LoginCheckerService } from '../../_helpers/login-checker.service';
import { IArticle } from '../../_interfaces/article-interface.article';
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
  onChange(e) {
    console.log(e);
  }
  get_cat() {
    this._ApiService.getCategories().subscribe(data => {
      this.categories = data['objects'];
      // tslint:disable-next-line:no-debugger
      debugger;
    });
  }
}
