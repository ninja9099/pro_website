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

  base_url: string = 'http://127.0.0.1:8000/api/v1/?content_type=application/json';
  get_token: string  = this.base_url + 'api-token' 
  articles = this.base_url + 'articles/?format=json';
  articleRatingUrl = 'http://127.0.0.1:8000/api/v1/rating/';
  articleFollowingUrl = 'http://127.0.0.1:8000/api/v1/following/';
  home_resource = 'http://localhost:8000/api/v1/main/';
  recent_articles = 'http://127.0.0.1:8000/api/v1/main/index';
  categories = 'http://127.0.0.1:8000/api/v1/category';
  subcategories = 'http://127.0.0.1:8000/api/v1/subcategory/';
  post_article = 'http://127.0.0.1:8000/api/v1/article/';

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
    return this.http.get(this.recent_articles + '?limit=' + limit);
  }
  getCategories() {
    return this.http.get(this.categories);
  }
  getSubCategories(catagory_id) {
    return this.http.get(this.subcategories + '?catagory_id=' + catagory_id);
  }
  saveArticle(article): Observable<IArticle> {
    return this.http.post<any>(this.post_article, article);
  }
}
