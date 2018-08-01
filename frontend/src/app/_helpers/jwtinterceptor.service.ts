// import { Injectable } from '@angular/core';
// import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
// import { Observable } from 'rxjs';
// import { LoginService } from '../_services/login.service';

// @Injectable()
// export class JwtInterceptor implements HttpInterceptor {
//   intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
//     // add authorization header with jwt token if available
//     const currentUser = JSON.parse(localStorage.getItem('currentUser'));
//     if (currentUser && currentUser.token) {
//       request = request.clone({
//         setHeaders: {
//           Authorization: `Bearer ${currentUser.token}`
//         }
//       });
//     }

//     return next.handle(request);
//   }
// }


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
