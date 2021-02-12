import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { PageButtonComponent } from './components/elements/page-button/page-button.component';
import { UnopenedPageBtnComponent } from './components/elements/unopened-page-btn/unopened-page-btn.component';
import { ButtonComponent } from './components/elements/button/button.component';
import { TextComponent } from './components/elements/text/text.component';
import { LinkTextComponent } from './components/elements/link-text/link-text.component';
import { EmptyStarComponent } from './components/elements/empty-star/empty-star.component';
import { FullStarComponent } from './components/elements/full-star/full-star.component';
import { OffButtonComponent } from './components/elements/off-button/off-button.component';
import { LineComponent } from './components/elements/line/line.component';
import { InputFieldComponent } from './components/elements/input-field/input-field.component';
import { ChoiceFieldComponent } from './components/elements/choice-field/choice-field.component';

@NgModule({
  declarations: [
    AppComponent,
    PageButtonComponent,
    UnopenedPageBtnComponent,
    ButtonComponent,
    TextComponent,
    LinkTextComponent,
    EmptyStarComponent,
    FullStarComponent,
    OffButtonComponent,
    LineComponent,
    InputFieldComponent,
    ChoiceFieldComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
