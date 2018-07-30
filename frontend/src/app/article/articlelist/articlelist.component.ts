import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../_services/api.service';


@Component({
  templateUrl: './articlelist.component.html',
  styleUrls: ['./articlelist.component.css']
})
export class ArticleListComponent implements OnInit {
  private artilce_list: any[];
  private data:any[];

  constructor(private _route: ActivatedRoute, private _ApiService: ApiService) { }
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
