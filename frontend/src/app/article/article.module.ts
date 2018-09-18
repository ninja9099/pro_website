import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ArticleComponent } from './article.component';
import { RouterModule } from '@angular/router';
import { BlogWritterComponent } from './blog-writter/blog-writter.component';
import { ArticleListComponent } from './articlelist/articlelist.component';
import { FroalaEditorModule, FroalaViewModule } from 'angular-froala-wysiwyg';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { TagInputModule } from 'ngx-chips';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AuthGuard } from '../_guards/auth.guard';
import { CustomTagComponent } from '../_directives/tag.component';
import { LikeComponent } from '../_directives/like-component/like-component.component';
import { AngularFontAwesomeModule } from 'angular-font-awesome';
import { SafePipe } from '../_pipes/safe.pipe';


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    TagInputModule,
    BrowserAnimationsModule,
    AngularFontAwesomeModule,
    RouterModule.forChild([
      { path: 'articles', component: ArticleListComponent },
      { path: 'article/:id', component: ArticleComponent },
      { path: 'tags/:id', component: ArticleListComponent },
      { path: 'write_new', component: BlogWritterComponent,  canActivate: [AuthGuard]} ]),
    FroalaEditorModule.forRoot(), FroalaViewModule.forRoot()
  ],
  declarations: [ArticleComponent, BlogWritterComponent, ArticleListComponent, CustomTagComponent, LikeComponent, SafePipe]
})
export class ArticleModule { }
