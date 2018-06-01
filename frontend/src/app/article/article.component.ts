import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { GetArticlesService } from './get-articles.service';
@Component({
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent implements OnInit {

  constructor(private _route: ActivatedRoute, private _ArticleService: GetArticlesService) { }

  ngOnInit() {
    const id = +this._route.snapshot.paramMap.get('id');
  }

}
