import { Injectable } from '@angular/core';
// tslint:disable-next-line:import-blacklist
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { catchError, retry } from 'rxjs/operators';

@Injectable()
export class GetArticlesService {

  constructor(private http: HttpClient) {
   }
  articleUrl = 'http://127.0.0.1:8000/api/v1/article/';

  getArticle() {
    return this.http.get(this.articleUrl);
  }

}
