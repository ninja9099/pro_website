import { Component, OnInit, ViewContainerRef } from '@angular/core';
import { LoginService } from '../../_services/login.service';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators/first';
import { GlobalVars } from '../../app.component';
import { ToastsManager } from 'ng2-toastr';

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
              public _gvars: GlobalVars,
              public vcr: ViewContainerRef,
              public toastr: ToastsManager,
              ) {
                _gvars.context = 'login';
                this.toastr.setRootViewContainerRef(vcr);
              }

  ngOnInit() {
    if (this._gvars.isLoggedIn) {
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
        this.loading = false;
        if (data['is_authenticated']) {
          this.toastr.success('Login successfull!', 'Success!');
          this.router.navigateByUrl(this.returnUrl);
          this._gvars.isLoggedIn = true;
        } else {
          this._gvars.isLoggedIn = false;
        }
      },
      error => {
        this.toastr.error('INCORRECT userid And password combinations', 'Login faulure!');
        console.log('In correct userid and password combinations');
        this.loading = false;
      }
    );
   }
  get diagnostic() {
    return JSON.stringify(this.loginModel);
  }
}
