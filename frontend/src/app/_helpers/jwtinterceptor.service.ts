import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
import { Observable } from 'rxjs';
import { LoginService } from '../_services/login.service';

@Injectable()
export class JwtInterceptor implements HttpInterceptor {
  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // add authorization header with jwt token if available
    // tslint:disable-next-line:no-debugger
    debugger;
    const user = JSON.parse(localStorage.getItem('user'));
    const token = JSON.parse(localStorage.getItem('apikey'));

    if (user && token) {
      request = request.clone({
        setHeaders: {
            Authorization: `ApiKey ${user}: ${token}`
            // Authorization: ApiKey<username>: <api_key>
        }
      });
    }

    return next.handle(request);
  }
}


// @Injectable()
// export class ErrorInterceptor implements HttpInterceptor {
//       constructor(private loginService: LoginService) { }

//       intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
//             return next.handle(request).pipe(catchError(err => {
//                   if (err.status === 401) {
//                         // auto logout if 401 response returned from api
//                         this.loginService.logout();
//                         location.reload(true);
//                   }

//                   const error = err.error.message || err.statusText;
//                   return throwError(error);
//             }));
//       }
// }
