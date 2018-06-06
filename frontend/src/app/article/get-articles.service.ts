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
export class GetArticlesService {
  constructor(private http: HttpClient, private _route: ActivatedRoute) {
   }
  articleUrl = 'http://127.0.0.1:8000/api/v1/article/';
  getArticle(id) {
    // tslint:disable-next-line:no-debugger
    debugger;
    return this.http.get(this.articleUrl + id);
  }
}
