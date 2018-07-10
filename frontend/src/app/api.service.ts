import { Injectable, OnInit } from '@angular/core';
// tslint:disable-next-line:import-blacklist
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, retry } from 'rxjs/operators';
import { ActivatedRoute } from '@angular/router';


const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class ApiService {
  constructor(private http: HttpClient, private _route: ActivatedRoute) {
  }
  articleUrl = 'http://127.0.0.1:8000/api/v1/article/';

  articleRatingUrl = 'http://127.0.0.1:8000/api/v1/rating/';
  articleFollowingUrl = 'http://127.0.0.1:8000/api/v1/following/';
  getArticle(id) {
    return this.http.get(this.articleUrl + id);
  }
  getArticles(range, limit) {
    return this.http.get(this.articleUrl);
  }
}
