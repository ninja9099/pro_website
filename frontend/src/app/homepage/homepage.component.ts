import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { IArticle } from '../shared/article-interface.article';
import { IResponse } from '../shared/user-interface';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {

  private articles: IArticle[];
  private home_resources: any[];


  constructor(private _ApiService: ApiService ) { }
  ngOnInit() {
    const limit = 5;
    this.home();
    this.recent_articles(limit);
  }

  public home() {
    this._ApiService.getHomeResource().subscribe((data: IResponse) => {
      this.home_resources = data.objects;
      console.log(this.home_resources)

    });

  }

  public recent_articles(limit) {
    this._ApiService.getRecentArticles(limit).subscribe((data: IArticle[]) => {
      this.articles = data;
      console.log(this.articles);
    });
  }
}
