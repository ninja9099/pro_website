import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { IArticle } from '../_interfaces/article-interface.article';
import 'rxjs/Rx';

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
  tags = this.base_url + 'tags/';

  private catchError (error: any) {
    console.log('request/response Error', error);
    return Observable.throw(error.statusText);
  }

  private processData(res: Response) {
    let body = res;
    return body || {};
  }


  getArticle(id) {
    return this.http.get(this.articles + id).map(this.processData).catch(this.catchError);
  }

  getArticles(range, limit): Observable<any> {
    return this.http.get(this.articles).map(this.processData).catch(this.catchError);
  }

  getHomeResource(): Observable<any> {
    return this.http.get(this.home_resource).map(this.processData).catch(this.catchError);
  }

  getRecentArticles(limit): Observable<any> {
    return this.http.get(this.recent_articles + '&limit=' + limit).map(this.processData).catch(this.catchError);
  }
  getCategories(): Observable<any> {
    return this.http.get(this.categories).map(this.processData).catch(this.catchError);
  }
  getSubCategories(catagory_id): Observable<any> {
    return this.http.get(this.subcategories + '&catagory_id=' + catagory_id).map(this.processData).catch(this.catchError);
  }
  saveArticle(article): Observable<IArticle> {
    return this.http.post<any>(this.post_article, article).map(this.processData).catch(this.catchError);
  }
  updateArticle(article, id) {
    return this.http.put<any>(this.post_article + id + '/', article).map(this.processData).catch(this.catchError);
  }
  getTag(id) {
    return this.http.get(this.tags + id + '/').map(this.processData).catch(this.catchError);
  }
}
