import { Component, OnInit } from '@angular/core';
import { LoginService } from '../../_services/login.service';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators/first';
import { AlertService } from '../../_services/alert.service';
import { GlobalVars } from '../../app.component';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})


export class LoginComponent implements OnInit {

  loginForm: FormGroup;
  loading = false;
  loginModel = {};
  submitted = false;
  returnUrl: string;


  constructor(private _loginservice: LoginService,
              private route: ActivatedRoute,
              private formBuilder: FormBuilder,
              private router: Router,
              public _alert: AlertService,
              public _gvars: GlobalVars,
              ) {
                _gvars.context = 'login';
              }

  ngOnInit() {
    if (this._gvars.isLoggedIn) {
      // tslint:disable-next-line:no-debugger
      debugger;
      this.router.navigate(['/']);
    }
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });

    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }

  get f() { return this.loginForm.controls; }

  onSubmit() {
    this.submitted = true;
    if (this.loginForm.invalid) {
      return;
    }
    this.loading = true;
    this._loginservice.login(this.f.username.value, this.f.password.value)
      .pipe(first()).subscribe(data => {
        // tslint:disable-next-line:no-debugger
        debugger;
        this.loading = false;
        if (data['is_authenticated']) {
          this._alert.success(data['message']);
          // this.router.navigate([this.returnUrl]);
          this.router.navigateByUrl(this.returnUrl);
          this._gvars.isLoggedIn = true;
        } else {
          this._alert.error(data['message']);
          this._gvars.isLoggedIn = false;
        }
      },
      error => {
        console.log('login failure wrong userid nd password combinations');
        this.loading = false;
      }
    );
   }
  get diagnostic() {
    return JSON.stringify(this.loginModel);
  }
}
