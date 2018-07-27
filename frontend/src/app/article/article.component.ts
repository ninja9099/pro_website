import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';
import { IArticle } from '../shared/article-interface.article';
@Component({
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent implements OnInit {

  private article: IArticle[];
  private article_followings: any[];
  private article_author: any[];
  private artilce_list: any[];

  constructor(private _route: ActivatedRoute, private _ApiService: ApiService) { }
  ngOnInit() {
    const id = +this._route.snapshot.paramMap.get('id');
    this.getArticle(id);
  }

  public getArticle(article_id) {
    this._ApiService.getArticle(article_id).subscribe((data: IArticle[]) => {
      this.article = data;
    });
  }
}
