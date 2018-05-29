import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { NewsletterComponent } from './newsletter/newsletter.component';
import { ArticleComponent } from './article/article.component';
import { AuthorProfileComponent } from './author-profile/author-profile.component';
import { BlogWritterComponent } from './blog-writter/blog-writter.component';
import { CommentComponent } from './shared/comment/comment.component';
import { HomepageComponent } from './homepage/homepage.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { AngularFontAwesomeModule } from 'angular-font-awesome';
import { ArticleModule } from './article/article.module';
import { RouterModule } from '@angular/router';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent,
    NewsletterComponent,
    AuthorProfileComponent,
    BlogWritterComponent,
    CommentComponent,
    HomepageComponent,
    PageNotFoundComponent,
  ],
  imports: [
    BrowserModule,
    AngularFontAwesomeModule,
    ArticleModule,
    RouterModule.forRoot([
      { path: '', component: HomepageComponent },
      { path: '**', component: PageNotFoundComponent }, ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
