import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { ApiService } from '../../_services/api.service';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
    selector: 'app-user-profile',
    styleUrls: ['./user-profile.component.css'],
    templateUrl: './user-profile.component.html',
})
export class UserProfileComponent implements OnInit{

    user: object;
    params: string;
    user_articles: object[];
    user_id: number;
    constructor(
        private _router: ActivatedRoute,
        private _apiService: ApiService,
        private _sanitizer: DomSanitizer
        ) {
    }

    ngOnInit() {
        this.params = this._router.snapshot.paramMap.get('id');
        this.getUserDetails(this.params);
        this.getArrticleWritten(this.params);
    }
    getUserDetails(id){
        this._apiService.getUser(id).subscribe(data => {
            console.log('this is user profile');
            this.user = data;
        },
        error => {
            console.log('error is ==> ' + error);
        });
    }
    getArrticleWritten(author_id) {
        this._apiService.getArticles(null, null, '&article_author=' + author_id + '&limit=' + 8).subscribe(data => {

            if (data.hasOwnProperty('results')) {
                this.user_articles = data.results;
            } else{
                this.user_articles = data;
            }
        });
    }
    getSantizeUrl(url: string) {
        return this._sanitizer.bypassSecurityTrustUrl(url);
    }
}
