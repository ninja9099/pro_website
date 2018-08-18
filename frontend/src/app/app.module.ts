import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent, GlobalVars } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
// import { ArticleComponent } from './article/article.component';
import { CommentComponent } from './shared/comment/comment.component';
import { HomepageComponent } from './homepage/homepage.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { AngularFontAwesomeModule } from 'angular-font-awesome';
import { ArticleModule } from './article/article.module';
import { RouterModule } from '@angular/router';
import { ApiService } from './_services/api.service';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { UserModule } from './user/user.module';
import { FormsModule, FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { LoginService } from './_services/login.service';
import { AlertComponent } from './alert/alert.component';
import { AlertService } from './_services/alert.service';
import { AuthGuard } from './_guards/auth.guard';
import { LoginCheckerService } from './_helpers/login-checker.service';
import { JwtInterceptor } from './_helpers/jwtinterceptor.service';
import {ToastModule} from 'ng2-toastr/ng2-toastr';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent,
    CommentComponent,
    HomepageComponent,
    PageNotFoundComponent,
    AlertComponent,
  ],
  imports: [
    BrowserModule,
    AngularFontAwesomeModule,
    ArticleModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    UserModule,
    ToastModule.forRoot(),
    RouterModule.forRoot([
      { path: '', component: HomepageComponent, canActivate: [AuthGuard] },
      { path: '**', component: PageNotFoundComponent }, ])
  ],
  providers: [
    ApiService,
    LoginService,
    FormBuilder,
    AlertService,
    AuthGuard,
    GlobalVars,
    LoginCheckerService,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: JwtInterceptor,
      multi: true
    },

  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
