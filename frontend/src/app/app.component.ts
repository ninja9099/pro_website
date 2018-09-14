import { Component, Injectable, OnInit, HostListener } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})



export class AppComponent {
  title = 'life-ina-bits';
}


@Injectable()
export class GlobalVars implements OnInit {
  public isLoggedIn;
  public user: string;
  public context: string ;
  ngOnInit() {
    if (localStorage.getItem('user')) {
      this.isLoggedIn = true;
      this.user = localStorage.getItem('user_id');
    }
  }
}
