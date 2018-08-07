import { Component, Injectable, OnInit } from '@angular/core';

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
  public context: string ;

  ngOnInit() {
    if (localStorage.getItem('user')) {
      this.isLoggedIn = true;
    }
  }
}
