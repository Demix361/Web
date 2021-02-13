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
import { LoginComponent } from './components/login/login.component';
import {FormsModule} from '@angular/forms';
import {RouterModule} from '@angular/router';
import { BaseComponent } from './components/base/base.component';
import { CartComponent } from './components/cart/cart.component';
import { ShopComponent } from './components/shop/shop.component';
import { UserComponent } from './components/user/user.component';
import { UsersComponent } from './components/users/users.component';
import { LogoutComponent } from './components/users/logout/logout.component';
import { ProfileComponent } from './components/users/profile/profile.component';
import { RegisterComponent } from './components/users/register/register.component';
import { ProductDetailComponent } from './components/shop/product-detail/product-detail.component';
import { ProductListComponent } from './components/shop/product-list/product-list.component';
import { ProductcategoryListComponent } from './components/shop/productcategory-list/productcategory-list.component';
import { CartListComponent } from './components/cart/cart-list/cart-list.component';
import { OrderDetailComponent } from './components/cart/order-detail/order-detail.component';
import { OrderFormComponent } from './components/cart/order-form/order-form.component';
import { OrderListComponent } from './components/cart/order-list/order-list.component';

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
    ChoiceFieldComponent,
    LoginComponent,
    // BaseComponent,
    CartComponent,
    ShopComponent,
    // UserComponent,
    UsersComponent,
    LogoutComponent,
    ProfileComponent,
    RegisterComponent,
    ProductDetailComponent,
    ProductListComponent,
    ProductcategoryListComponent,
    CartListComponent,
    OrderDetailComponent,
    OrderFormComponent,
    OrderListComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
