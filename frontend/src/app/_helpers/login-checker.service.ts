import { Injectable, OnInit } from '@angular/core';
import { GlobalVars } from '../app.component';

@Injectable()
export class LoginCheckerService {

  constructor(private _gvars: GlobalVars) { }
  is_loggedin() {
    if (localStorage.getItem('user')) {
      return true ;
    } else {
      return false ;
    }
  }
}
