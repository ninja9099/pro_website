import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { ApiService } from '../../_services/api.service';

@Component({
    selector: 'app-user-profile',
    styleUrls: ['./user-profile.component.css'],
    templateUrl: './user-profile.component.html',
})
export class UserProfileComponent implements OnInit{

    user: object;
    params: string;
    constructor(
        private _router: ActivatedRoute,
        private _apiService: ApiService) {
    }
    ngOnInit() {
        debugger;
        this.params = this._router.snapshot.paramMap.get('id');
        this.getUserDetails(this.params);
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
}