import { Component, OnInit } from '@angular/core';
import { ApiService } from '../_services/api.service';
import { IArticle } from '../_interfaces/article-interface.article';
import { IResponse } from '../_interfaces/user-interface';
import { AlertService } from '../_services/alert.service';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {

  private articles: IArticle[];
  private home_resources: any[];


  constructor(private _ApiService: ApiService, private _alert: AlertService) { }
  ngOnInit() {
    const limit = 5;
    this.recent_articles(limit);
    const context: string = localStorage.getItem('context') || 'home';
    $('#' + context).addClass('active');
  }

  public home() {
    this._ApiService.getHomeResource().subscribe((data: IResponse) => {
      this.home_resources = data.objects;
      console.log(this.home_resources);

    });

  }

  public recent_articles(limit) {
    this._ApiService.getRecentArticles(limit).subscribe((data: IArticle[]) => {
      this.articles = data;
      console.log(this.articles);
    });
  }
}
