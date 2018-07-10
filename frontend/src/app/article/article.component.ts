import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent implements OnInit {
  private article: Array<object> = [];
  private article_followings: any[];
  private article_author: any[];
  private artilce_list: any[];

  constructor(private _route: ActivatedRoute, private _ApiService: ApiService) { }
  ngOnInit() {
    const id = +this._route.snapshot.paramMap.get('id');
    this.getArticle(id);
  }

  public getArticle(article_id) {
    this._ApiService.getArticle(article_id).subscribe((data: Array<object>) => {
      this.article = data;
      console.log(this.article);
    });
  }
}
