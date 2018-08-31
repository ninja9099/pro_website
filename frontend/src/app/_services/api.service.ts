import { Injectable } from '@angular/core';
// tslint:disable-next-line:import-blacklist
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { IArticle } from '../_interfaces/article-interface.article';


const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class ApiService {
  constructor(private http: HttpClient, private _route: ActivatedRoute) {
  }

  format = '?format=json';
  base_url = 'http://127.0.0.1:8000/api/v1/';
  get_token: string = this.base_url + 'api-token' + this.format;
  articles = this.base_url + 'articles/' + this.format;
  articleRatingUrl = 'http://127.0.0.1:8000/api/v1/rating/' + this.format;
  articleFollowingUrl = 'http://127.0.0.1:8000/api/v1/following/' + this.format;
  home_resource = 'http://localhost:8000/api/v1/main/' + this.format;
  recent_articles = 'http://127.0.0.1:8000/api/v1/main/index' + this.format;
  categories = 'http://127.0.0.1:8000/api/v1/category/' + this.format;
  subcategories = 'http://127.0.0.1:8000/api/v1/subcategory/' + this.format;
  post_article = 'http://127.0.0.1:8000/api/v1/articles/';

  getArticle(id) {
    return this.http.get(this.articles + id);
  }

  getArticles(range, limit) {
    return this.http.get(this.articles);
  }

  getHomeResource() {
    return this.http.get(this.home_resource);
  }

  getRecentArticles(limit) {
    return this.http.get(this.recent_articles + '&limit=' + limit);
  }
  getCategories() {
    return this.http.get(this.categories);
  }
  getSubCategories(catagory_id) {
    return this.http.get(this.subcategories + '&catagory_id=' + catagory_id);
  }
  saveArticle(article): Observable<IArticle> {
    return this.http.post<any>(this.post_article, article);
  }
  updateArticle(article, id) {
    return this.http.put<any>(this.post_article + id + '/', article);
  }
}
