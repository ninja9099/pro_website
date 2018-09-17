import { Component, OnInit, HostListener, TemplateRef, ElementRef, AfterViewInit } from '@angular/core';
import { LoginService } from '../_services/login.service';
import { GlobalVars } from '../app.component';
import {
  trigger,
  state,
  style,
  animate,
  transition
} from '@angular/animations';
import { Router, NavigationEnd } from '@angular/router';



@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
  animations: [
    trigger('navAnimation', [
      state('fixed', style({
        transform: 'translateY(0px)'
      })),
      state('notfixed', style({
        transform: 'translateY(-100px)'
      })),
      transition('fixed <=> notfixed', animate('300ms ease-in'))
    ])
  ]
})
export class NavbarComponent  implements OnInit {

  public context: string = localStorage.getItem('context');
  public navIsFixed: boolean = false;
  public navIsNotFixed: boolean = false;
  public isLoggedIn: boolean;
  state: string = 'fixed';
  lastScrollTop = 0;
  st = 0;
  public user = localStorage.getItem('user_id');

  constructor(
    private _loginService: LoginService,
    public _gvars: GlobalVars,
    private _router: Router,
     ) {
      _router.events.subscribe((val) => {
        this.navIsFixed = false;
        this.state = 'fixed'
        console.log(val instanceof NavigationEnd) 
    });
     }
  logOut() {
    this._loginService.logout();
    this._gvars.isLoggedIn = false;
    location.reload();
  }

  ngOnInit(): void {
   if (this._loginService._doCheckLogin()) {
     this._gvars.isLoggedIn = true;
   }
  }


  @HostListener('window:scroll', ['$event'])
  doSomething(event) {
    this.st = window.pageYOffset;

    if (this.st > this.lastScrollTop) {
      console.log('down');
      if (window.pageYOffset >= 200) {
        this.state = 'notfixed';
      }
    } else if (this.st === this.lastScrollTop) {
      console.log('passing the IE just Ignore')
    } else {
      console.log('up');
      if (window.pageYOffset !== 0) {
        this.state = 'fixed';
        this.navIsFixed = true;
      } else {
        this.navIsFixed = false;
      }
    }
    this.lastScrollTop = this.st;
  }
}


