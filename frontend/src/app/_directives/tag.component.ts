import { Directive, Input, OnInit, Component, OnChanges, AfterContentInit } from '@angular/core';
import { ApiService } from '../_services/api.service';
import { takeWhile } from 'rxjs/operators';

@Component({
    selector: 'app-tag',
    templateUrl: './tag.component.html',
    styleUrls: ['./tag.component.css'],
})
export class CustomTagComponent implements OnInit, OnChanges {

    @Input() tagid: number;
    public tag: object;

    @Input() behaveClass: string;

    constructor(private _apiService: ApiService, ) {

    }

    ngOnChanges() {
    }

    ngOnInit() {
        this._apiService.getTag(this.tagid).subscribe(data => {
            this.tag = data;
        },
            error => {
                console.log('unable to get the tag details for the tag' + this.tagid);
            });
    }
}
