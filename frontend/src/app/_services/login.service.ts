import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable()
export class LoginService {

  constructor(private http: HttpClient) { }

  login(username: string, password: string) {
    const body = { user: username, password: password };
    // tslint:disable-next-line:no-debugger
    return this.http.post('http://localhost:8000/api/v1/user/login', body).pipe(map(response => {

      // login successful if there's a user and  token in the response
      if (response && response['apikey'] && response['user']) {
        // store user details and  token in local storage to keep user logged in between page refreshes
        localStorage.setItem('user', JSON.stringify(response['user']));
        localStorage.setItem('apikey', JSON.stringify(response['apikey']));
        localStorage.setItem('user_resource', JSON.stringify(response['user_resource']));
      }
      return response;
    }
  ));
}
  logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
    localStorage.removeItem('apikey');
  }
}
