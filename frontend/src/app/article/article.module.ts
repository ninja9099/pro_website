import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ArticleComponent } from './article.component';
import { RouterModule } from '@angular/router';
import { BlogWritterComponent } from './blog-writter/blog-writter.component';
import { ArticleListComponent } from './articlelist/articlelist.component';
import { FroalaEditorModule, FroalaViewModule } from 'angular-froala-wysiwyg';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forChild([
      { path: 'articles', component: ArticleListComponent },
      { path: 'article/:id', component: ArticleComponent },
      { path: 'write_new', component: BlogWritterComponent} ]),
    FroalaEditorModule.forRoot(), FroalaViewModule.forRoot()
  ],
  declarations: [ArticleComponent, BlogWritterComponent, ArticleListComponent,]
})
export class ArticleModule { }
