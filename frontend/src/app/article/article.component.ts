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
  constructor(private _route: ActivatedRoute, private _ApiService: ApiService) { }
  ngOnInit() {
    const id = +this._route.snapshot.paramMap.get('id');
    this.getArticle(id);
    this.getFollowings(id);
  }

  public getArticle(article_id) {
    this._ApiService.getArticle(article_id).subscribe((data: Array<object>) => {
      this.article = data;
      console.log(this.article);
    });
  }
  public getFollowings(article_id) {
    this._ApiService.getArticleFollowings(article_id).subscribe((data: Array<object>) => {
      this.article_followings = data;
      console.log(this.article_followings);
    });
  }
}
