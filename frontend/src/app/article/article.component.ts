import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { GetArticlesService } from './get-articles.service';

@Component({
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent implements OnInit {
  public article;
  constructor(private _route: ActivatedRoute, private _ArticleService: GetArticlesService) { }
  ngOnInit() {
    const id = +this._route.snapshot.paramMap.get('id');

    this._ArticleService.getArticle(id).subscribe(
      data => {this.article = data;
      },
      err => console.error(err),
      () => console.log('done loading foods')
    );
  }

}
