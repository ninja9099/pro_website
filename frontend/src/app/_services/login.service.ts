import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable()
export class LoginService {

  constructor(private http: HttpClient) { }

  login(username: string, password: string) {
    const body = { user: username, password: password };
    // tslint:disable-next-line:no-debugger
    debugger;
    return this.http.post('http://localhost:8000/api/v1/user/login', body).pipe(map(user => {
      // login successful if there's a jwt token in the response
      // tslint:disable-next-line:no-debugger
      debugger;
      if (user && user.token) {
        // store user details and jwt token in local storage to keep user logged in between page refreshes
        localStorage.setItem('currentUser', JSON.stringify(user));
      }
      return user;
    }
  ));
}
  logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('currentUser');
  }
}
