import { Injectable, OnInit } from '@angular/core';
// tslint:disable-next-line:import-blacklist
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, retry } from 'rxjs/operators';


const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class GetArticlesService {
  constructor(private http: HttpClient) {
   }
  articleUrl = 'http://127.0.0.1:8000/api/v1/article/';

  getArticles() {
    return this.http.get(this.articleUrl);
  }
}
