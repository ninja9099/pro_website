import { Component, OnInit } from '@angular/core';
import { LoginService } from '../../_services/login.service';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators/first';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})


export class LoginComponent implements OnInit {

  loading = false;
  loginModel = {};
  submitted = false;
  returnUrl: string;
  loginform: FormGroup;

  constructor(private _loginservice: LoginService,
              private route: ActivatedRoute,
              private formBuilder: FormBuilder,
              private router: Router,
              ) { }

  ngOnInit() {
    this.loginform = this.formBuilder.group({
      email: ['', Validators.required],
      password: ['', Validators.required]
    });
    this._loginservice.logout();
    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }

  get f() { return this.loginform.controls; }

  onSubmit() {
    this.submitted = true;
    if (this.loginform.invalid) {
      // tslint:disable-next-line:no-debugger
      debugger;
      return;
    }
    this.loading = true;
    this._loginservice.login(this.f.email.value, this.f.password.value)
      .pipe(first()).subscribe(data => {
        this.router.navigate([this.returnUrl]);
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
