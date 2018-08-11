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

  articleUrl = 'http://127.0.0.1:8000/articles/?format=json&username=pam&password=pankaj@123';
  articleRatingUrl = 'http://127.0.0.1:8000/api/v1/rating/';
  articleFollowingUrl = 'http://127.0.0.1:8000/api/v1/following/';
  home_resource = 'http://localhost:8000/api/v1/main/';
  recent_articles = 'http://127.0.0.1:8000/api/v1/main/index';
  categories = 'http://127.0.0.1:8000/api/v1/category';
  subcategories = 'http://127.0.0.1:8000/api/v1/subcategory/';
  post_article = 'http://127.0.0.1:8000/api/v1/article/';

  getArticle(id) {
    return this.http.get(this.articleUrl + id);
  }

  getArticles(range, limit) {
    return this.http.get(this.articleUrl);
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
