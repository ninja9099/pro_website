import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { NewsletterComponent } from './newsletter/newsletter.component';
import { ArticleComponent } from './article/article.component';
import { AuthorProfileComponent } from './author-profile/author-profile.component';
import { CommentComponent } from './shared/comment/comment.component';
import { HomepageComponent } from './homepage/homepage.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { AngularFontAwesomeModule } from 'angular-font-awesome';
import { ArticleModule } from './article/article.module';
import { RouterModule } from '@angular/router';
import { ApiService } from './api.service';
import { HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent,
    NewsletterComponent,
    AuthorProfileComponent,
    CommentComponent,
    HomepageComponent,
    PageNotFoundComponent,
  ],
  imports: [
    BrowserModule,
    AngularFontAwesomeModule,
    ArticleModule,
    HttpClientModule,
    RouterModule.forRoot([
      { path: '', component: HomepageComponent },
      { path: '**', component: PageNotFoundComponent }, ])
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
