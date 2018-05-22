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


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent,
    NewsletterComponent,
    ArticleComponent,
    AuthorProfileComponent,
    BlogWritterComponent,
    CommentComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
