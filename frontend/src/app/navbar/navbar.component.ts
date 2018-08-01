import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  public context: string = localStorage.getItem('context');

  constructor() { }

  ngOnInit() {
    $('#' + this.context).addClass('active');
  }
  onClick(e) {
    $('.active').removeClass('active');
    $('#' + this.context).addClass('active');
    localStorage.setItem('context', e.target.parentElement.id);
  }
}
