import { TestBed, inject } from '@angular/core/testing';

import { JwtinterceptorService } from './jwtinterceptor.service';

describe('JwtinterceptorService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [JwtinterceptorService]
    });
  });

  it('should be created', inject([JwtinterceptorService], (service: JwtinterceptorService) => {
    expect(service).toBeTruthy();
  }));
});
