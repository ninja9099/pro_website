import { Component, OnInit, ViewContainerRef } from '@angular/core';
import { ApiService } from '../_services/api.service';
import { IArticle } from '../_interfaces/article-interface.article';
import { IResponse } from '../_interfaces/user-interface';
import { AlertService } from '../_services/alert.service';
import { GlobalVars } from '../app.component';
import { LoginCheckerService } from '../_helpers/login-checker.service';
import { ToastsManager } from 'ng2-toastr/ng2-toastr';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {

  private articles: IArticle[];
  private home_resources: any[];

  constructor(private _ApiService: ApiService,
    private _alert: AlertService,
    public _gvars: GlobalVars,
    public _loginChecker: LoginCheckerService,
    public toastr: ToastsManager,
    public vcr: ViewContainerRef
  ) {
    this.toastr.setRootViewContainerRef(vcr);
    _gvars.context = 'home';
    if (_loginChecker.is_loggedin()) {
      _gvars.isLoggedIn = true;
    }

  }
  ngOnInit() {
    const limit = 10;
    this.recent_articles(limit);
  }

  public home() {
    this._ApiService.getHomeResource().subscribe((data: IResponse) => {
      this.home_resources = data.objects;
      console.log(this.home_resources);

    });

  }

  public recent_articles(limit) {
    this._ApiService.getRecentArticles(limit).subscribe((data: IArticle[]) => {
      debugger;
      this.articles = data;
      console.log(this.articles);
    });
  }
  public showToast() {
    this.toastr.success('You are awesome!', 'Success!');
    debugger;
  }
}
