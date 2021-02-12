import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EmptyStarComponent } from './empty-star.component';

describe('EmptyStarComponent', () => {
  let component: EmptyStarComponent;
  let fixture: ComponentFixture<EmptyStarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EmptyStarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EmptyStarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
