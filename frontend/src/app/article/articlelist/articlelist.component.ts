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
  
  public article_list: any[] = [];
  data: any[];
  context: string = localStorage.getItem('context');
  is_more: boolean;
  limit = 6;
  offset = 0;
  is_loading: boolean;


  constructor(private _route: ActivatedRoute,
    private _ApiService: ApiService,
    public _gvars: GlobalVars,
  ) {
    _gvars.context = 'blog';
   }
  ngOnInit() {
    this.get_article_list(null, 10);
  }


  get_article_list(limit, offset) {
    this._ApiService.getArticles({'limit': this.limit, 'offset': this.offset}).subscribe((data: Array<object>) => {
      debugger;
      this.offset = this.offset + 6;
      this.article_list = this.article_list.concat(data['results']);
      if (data['next']) {
        this.is_more = true;
      } else {
        this.is_more = false;
      }
      this.is_loading = false;
      console.log(data);
    });
  }

  loadMore(event) {
    this.is_loading = true;
    setTimeout(() => {
      this.get_article_list(null, 0);
    }, 3000);
  }
}
