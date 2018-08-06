import { Component, OnInit } from '@angular/core';
import { GlobalVars } from '../../app.component';

@Component({
  selector: 'app-blog-writter',
  templateUrl: './blog-writter.component.html',
  styleUrls: ['./blog-writter.component.css']
})
export class BlogWritterComponent implements OnInit {

  public editorContent = 'My Document\'s Title';
  constructor(public _gvars: GlobalVars) {
    _gvars.context = 'writer';
  }

  ngOnInit() {
    localStorage.setItem('context', 'writer');
  }

}
