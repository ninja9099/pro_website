import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BlogWritterComponent } from './blog-writter.component';

describe('BlogWritterComponent', () => {
  let component: BlogWritterComponent;
  let fixture: ComponentFixture<BlogWritterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BlogWritterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BlogWritterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
