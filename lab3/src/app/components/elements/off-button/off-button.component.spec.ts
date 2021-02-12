import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OffButtonComponent } from './off-button.component';

describe('OffButtonComponent', () => {
  let component: OffButtonComponent;
  let fixture: ComponentFixture<OffButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OffButtonComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OffButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
