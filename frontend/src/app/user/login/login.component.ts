import { Component, OnInit } from '@angular/core';
import { LoginService } from '../../_services/login.service';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators/first';
import { AlertService } from '../../_services/alert.service';

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
              ) { }

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
    this._loginservice.logout();
    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }

  get f() { return this.loginForm.controls; }

  onSubmit() {
    this.submitted = true;
    if (this.loginForm.invalid) {
      // tslint:disable-next-line:no-debugger
      debugger;
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
        } else {
          this._alert.error(data['message']);
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
