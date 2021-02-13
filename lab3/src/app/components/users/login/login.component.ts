import { Component, OnInit } from '@angular/core';
import {ServicesService} from '../../../services/services.service';
import {ActivatedRoute, Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  login = '';
  password = '';

  constructor() { }

  ngOnInit(): void {
  }

}
//
//
// import { Component, OnInit } from '@angular/core';
//
//
// @Component({
//   selector: 'app-login',
//   templateUrl: './login.component.html',
//   styleUrls: ['./login.component.scss']
// })
// export class LoginComponent implements OnInit {
//   login = '';
//   password = '';
//
//   constructor(private userService: UserService, private route: ActivatedRoute,
//               private router: Router) { }
//
//   ngOnInit(): void {
//   }
//
//   checkAuth() {
//     if (this.login !== '' && this.password !== '') {
//       this.userService.getLoginToken(this.login, this.password)
//         .subscribe(token => {
//             localStorage.setItem('object-detection-token', <string> token['token']);
//             localStorage.setItem('object-detection-current-user', this.login);
//             this.router.navigate(['/main']);
//           },
//           error => {
//             alert(error.status + ': ' + error.error);
//           });
//     }
//     else {
//       alert('Some fields are empty');
//     }
//   }
// }
//
