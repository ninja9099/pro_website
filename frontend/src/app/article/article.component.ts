import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../_services/api.service';
import { IArticle } from '../_interfaces/article-interface.article';
import { GlobalVars } from '../app.component';
@Component({
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent implements OnInit {

  private article: object;
  private article_followings: any[];
  private article_author: object;
  private artilce_list: any[];

  constructor(private _route: ActivatedRoute, private _apiService: ApiService) {
   }
  ngOnInit() {
    const id = +this._route.snapshot.paramMap.get('id');
    this.getArticle(id);
  }

  public getArticle(article_id) {
    this._apiService.getArticle(article_id).subscribe((data: object) => {
      this.article = data;
      this._apiService.getUser(this.article['article_author']).subscribe(data => {
          // tslint:disable-next-line:no-debugger
          debugger;
      },
      error =>{
        console.log('could not get the data try again later');
      });
    });
  }
}
