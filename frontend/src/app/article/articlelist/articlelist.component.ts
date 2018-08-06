import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../_services/api.service';
import { GlobalVars } from '../../app.component';


@Component({
  templateUrl: './articlelist.component.html',
  styleUrls: ['./articlelist.component.css']
})
export class ArticleListComponent implements OnInit {
  private artilce_list: any[];
  private data: any[];
  public context: string = localStorage.getItem('context');

  constructor(private _route: ActivatedRoute, private _ApiService: ApiService, public _gvars: GlobalVars) { 
    _gvars.context = 'blog';
   }
  ngOnInit() {

    this.get_article_list(null, 10);
  }
  public get_article_list(range, limit) {
    this._ApiService.getArticles(null, limit).subscribe((data: Array<object>) => {
      // tslint:disable-next-line:no-debugger
      debugger;
      this.artilce_list = data['objects'];
      console.log(data);
    });
  }
}
