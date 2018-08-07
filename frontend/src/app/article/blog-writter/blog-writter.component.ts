import { Component, OnInit } from '@angular/core';
import { GlobalVars } from '../../app.component';
import { LoginCheckerService } from '../../_helpers/login-checker.service';
@Component({
  selector: 'app-blog-writter',
  templateUrl: './blog-writter.component.html',
  styleUrls: ['./blog-writter.component.css']
})
export class BlogWritterComponent implements OnInit {

  public editorContent = 'My Document\'s Title';
  constructor(public _gvars: GlobalVars, public _loginChecker: LoginCheckerService) {
    _gvars.context = 'writer';
    // tslint:disable-next-line:no-debugger
    if (_loginChecker.is_loggedin()) {
      _gvars.isLoggedIn = true;
    }
  }

  ngOnInit() {
    localStorage.setItem('context', 'writer');
  }

}
