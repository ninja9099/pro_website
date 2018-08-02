import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-blog-writter',
  templateUrl: './blog-writter.component.html',
  styleUrls: ['./blog-writter.component.css']
})
export class BlogWritterComponent implements OnInit {

  public editorContent = 'My Document\'s Title';
  public context: string = localStorage.getItem('context');
  constructor() { }

  ngOnInit() {
    $('.active').removeClass('active');
    localStorage.setItem('context', 'writer');
    $('#' + this.context).addClass('active');
  }

}
