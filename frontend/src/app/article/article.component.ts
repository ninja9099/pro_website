import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../_services/api.service';
import { GlobalVars } from '../app.component';

import { DomSanitizer } from '@angular/platform-browser';
@Component({
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent implements OnInit {

  private article: object;
  private article_followings: any[];
  private article_author: object;
  private artilce_list: any[];

  constructor(private _route: ActivatedRoute,
    private _apiService: ApiService,
    private _sanitizer: DomSanitizer) {
   }
  ngOnInit() {
    const id = +this._route.snapshot.paramMap.get('id');
    this.getArticle(id);
  }

  public getSantizeUrl(url: string) {
    return this._sanitizer.bypassSecurityTrustUrl(url);
  }

  public getArticle(article_id) {
    this._apiService.getArticle(article_id).subscribe((data: object) => {
      this.article = data;
      this._apiService.getUser(this.article['article_author']).subscribe(userData => {
        this.article_author = userData;
      },
      error => {
        console.log('could not get the data try again later');
      });
    });
  }
}
