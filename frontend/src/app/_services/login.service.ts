import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable()
export class LoginService {

  constructor(private http: HttpClient) { }

  login(username: string, password: string) {
    const body = { username: username, password: password};
    // tslint:disable-next-line:no-debugger
    return this.http.post('http://127.0.0.1:8000/api/v1/api-token/',body
  ).pipe(map(response => {
      // login successful if there's a user and  token in the response
      if (response && response['token'] && response['user']) {
        // store user details and  token in local storage to keep user logged in between page refreshes
        localStorage.setItem('user', JSON.stringify(response['user']));
        localStorage.setItem('user_id', JSON.stringify(response['id']));
        localStorage.setItem('apikey', JSON.stringify(response['token']));
      }
      return response;
    }
  ));
}
  logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
    localStorage.removeItem('apikey');
    localStorage.removeItem('user_id');
  }
}
