import { TestBed, inject } from '@angular/core/testing';

import { LoginCheckerService } from './login-checker.service';

describe('LoginCheckerService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [LoginCheckerService]
    });
  });

  it('should be created', inject([LoginCheckerService], (service: LoginCheckerService) => {
    expect(service).toBeTruthy();
  }));
});
