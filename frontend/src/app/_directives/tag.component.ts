import { Directive, Input, OnInit, Component } from '@angular/core';
import { ApiService } from '../_services/api.service';

@Component({
    selector: 'app-tag',
    template: `<a class='tags' [routerLink] ="['/tags/', tag.id]">{{tag.name}}</a>`,
    styleUrls: ['./tag.component.css'],
})
export class CustomTagComponent implements OnInit {

    @Input() tagid: number;
    tag: any;
    constructor(private _apiService: ApiService, ) {
    }

    ngOnInit() {
        // tslint:disable-next-line:no-debugger
        debugger;
        this._apiService.getTag(this.tagid).subscribe(data => {
            this.tag = data;
        },
        error => {
            console.log('unable to get the tag details for the tag' + this.tagid);
        });
    }
}
