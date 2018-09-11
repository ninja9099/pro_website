import { Directive, Input, OnInit, Component, OnChanges } from '@angular/core';
import { ApiService } from '../_services/api.service';

@Component({
    selector: 'app-tag',
    template: `<a class='tags' [routerLink] ="['/tags/', tagid]">{{tag.name}}</a>`,
    styleUrls: ['./tag.component.css'],
})
export class CustomTagComponent implements OnInit, OnChanges {

    @Input() tagid: number;
    public tag: object;
    constructor(private _apiService: ApiService,) {
    }

    ngOnChanges() {
        this._apiService.getTag(this.tagid).subscribe(data => {
            this.tag = data;
        },
        error => {
            console.log('unable to get the tag details for the tag' + this.tagid);
        });
    }

    ngOnInit() {
        // this._apiService.getTag(this.tagid).subscribe(data => {
        //     this.tag = data;
        // },
        // error => {
        //     console.log('unable to get the tag details for the tag' + this.tagid);
        // });
    }
}
