import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FullStarComponent } from './full-star.component';

describe('FullStarComponent', () => {
  let component: FullStarComponent;
  let fixture: ComponentFixture<FullStarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FullStarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FullStarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
