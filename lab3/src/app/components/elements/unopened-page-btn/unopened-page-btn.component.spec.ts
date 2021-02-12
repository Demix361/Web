import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UnopenedPageBtnComponent } from './unopened-page-btn.component';

describe('UnopenedPageBtnComponent', () => {
  let component: UnopenedPageBtnComponent;
  let fixture: ComponentFixture<UnopenedPageBtnComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UnopenedPageBtnComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(UnopenedPageBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
