import { Injectable, ViewContainerRef } from '@angular/core';
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { IArticle } from '../_interfaces/article-interface.article';
import 'rxjs/Rx';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};


@Injectable()
export class ApiService {
  constructor(private http: HttpClient,
    private _route: ActivatedRoute,
   ) {}

  format = '?format=json';
  base_url = 'http://127.0.0.1:8000/api/v1/';
  get_token: string = this.base_url + 'api-token' + this.format;
  articleRatingUrl = 'http://127.0.0.1:8000/api/v1/rating/' + this.format;
  articleFollowingUrl = 'http://127.0.0.1:8000/api/v1/following/' + this.format;
  categories = 'http://127.0.0.1:8000/api/v1/category/' + this.format;
  subcategories = 'http://127.0.0.1:8000/api/v1/subcategory/' + this.format;
  post_article = 'http://127.0.0.1:8000/api/v1/articles/';
  tags = this.base_url + 'tags/';

  private catchError(error: HttpErrorResponse) {
    if (error instanceof HttpErrorResponse) {
      Object.keys(error).forEach(data => {
          if (data === 'error') {
            console.log(error[data]);
          }
        });
    }
    console.log('request/response Error', error);
    return Observable.throw(error);
  }

  private processData(res: Response) {
    let body = res;
    return body || {};
  }

  private getQueryString(params) {
    let q_str = '';
    for (let key in params) {
      if (params.hasOwnProperty(key)) {
        q_str = q_str + `&${key}=${params[key]}`;
      }
    }
    return q_str;
  }


  getUser(id) {
    return this.http.get(this.base_url + 'users/' + id + this.format).map(this.processData).catch(this.catchError);
  }

  getArticle(id) {
    return this.http.get(this.base_url + 'articles/' + id + this.format).map(this.processData).catch(this.catchError);
  }

  getArticles(params: object): Observable<any> {
    const query_string = this.getQueryString(params);
    return this.http.get(this.base_url + 'articles/' + this.format + query_string).map(this.processData).catch(this.catchError);
  }


  getCategories(): Observable<any> {
    return this.http.get(this.categories).map(this.processData).catch(this.catchError);
  }

  getSubCategories(catagory_id, params): Observable<any> {
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

  likeObject(objectid, likeobject): Observable <any> {
    return this.http.put(this.base_url + 'likes/' + objectid + '/', likeobject);
  }
}
