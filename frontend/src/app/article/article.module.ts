import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ArticleComponent } from './article.component';
import { RouterModule } from '@angular/router';

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild([
      { path: 'articles', component: ArticleComponent },
      { path: 'article/:id', component: ArticleComponent },])
  ],
  declarations: [ArticleComponent]
})
export class ArticleModule { }
