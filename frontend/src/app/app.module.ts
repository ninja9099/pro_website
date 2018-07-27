import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { ArticleComponent } from './article/article.component';
import { CommentComponent } from './shared/comment/comment.component';
import { HomepageComponent } from './homepage/homepage.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { AngularFontAwesomeModule } from 'angular-font-awesome';
import { ArticleModule } from './article/article.module';
import { RouterModule } from '@angular/router';
import { ApiService } from './api.service';
import { HttpClientModule } from '@angular/common/http';
import { UserModule } from './user/user.module';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent,
    CommentComponent,
    HomepageComponent,
    PageNotFoundComponent,
  ],
  imports: [
    BrowserModule,
    AngularFontAwesomeModule,
    ArticleModule,
    HttpClientModule,
    UserModule,
    RouterModule.forRoot([
      { path: '', component: HomepageComponent },
      { path: '**', component: PageNotFoundComponent }, ])
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
