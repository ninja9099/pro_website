import { Component, OnInit } from '@angular/core';
import { LoginService } from '../_services/login.service';
import { GlobalVars } from '../app.component';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {

  public context: string = localStorage.getItem('context');
  constructor(private _loginService: LoginService, public _gvars: GlobalVars, ) { }


  logOut() {
    this._loginService.logout();
    this._gvars.isLoggedIn = false;
  }
}
