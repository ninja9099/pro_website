import { TestBed, inject } from '@angular/core/testing';

import { GetArticlesService } from './get-articles.service';

describe('GetArticlesService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GetArticlesService]
    });
  });

  it('should be created', inject([GetArticlesService], (service: GetArticlesService) => {
    expect(service).toBeTruthy();
  }));
});
