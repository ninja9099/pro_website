import { Component, OnInit, Input } from '@angular/core';
import { ApiService } from '../../_services/api.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-like-component',
  templateUrl: './like-component.component.html',
  styleUrls: ['./like-component.component.css']
})
export class LikeComponent implements OnInit {
  likeObject = { user_id: null, article_id: null, is_liked: null};

  @Input() objectid: number;
  constructor(private _apiService: ApiService) { }

  ngOnInit() {
  }

  likedArticle(objectid: number) {
    this.likeObject.user_id = localStorage.getItem('user_id');
    this.likeObject.article_id = this.objectid;
    this.likeObject.is_liked = true;

    this._apiService.likeObject(this.objectid, JSON.stringify(this.likeObject)).subscribe((data: Object) => {
      // tslint:disable-next-line:no-debugger
      debugger;
    },
    error => {
      console.log(error);
     });

  }
}
