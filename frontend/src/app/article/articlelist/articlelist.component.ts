import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../_services/api.service';
import { GlobalVars } from '../../app.component';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  templateUrl: './articlelist.component.html',
  styleUrls: ['./articlelist.component.css']
})
export class ArticleListComponent implements OnInit {
  public article_list: any[];
  public data: any[];
  public context: string = localStorage.getItem('context');

  constructor(private _route: ActivatedRoute,
    private _ApiService: ApiService,
    public _gvars: GlobalVars,
  ) {
    _gvars.context = 'blog';
   }
  ngOnInit() {
    this.get_article_list(null, 10);
  }
  public get_article_list(range, limit) {
    this._ApiService.getArticles(null, limit).subscribe((data: Array<object>) => {
      this.article_list = data['results'];
      console.log(data);
    });
  }
}
