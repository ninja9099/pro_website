import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ArticleComponent } from './article.component';
import { RouterModule } from '@angular/router';
import { BlogWritterComponent } from './blog-writter/blog-writter.component';
import { ArticleListComponent } from './articlelist/articlelist.component';


@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild([
      { path: 'articles', component: ArticleListComponent },
      { path: 'article/:id', component: ArticleComponent },
      { path: 'write_new', component: BlogWritterComponent} ])
  ],
  declarations: [ArticleComponent, BlogWritterComponent, ArticleListComponent, ]
})
export class ArticleModule { }
