import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {User} from '../models/user.model';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ServicesService {
  private url = environment.baseUrl;
  constructor(private http: HttpClient) {
  }

  getLoginToken(login: string, password: string): Observable<User> {
    // let paramsList = new HttpParams();
    // paramsList = paramsList.append('username', login);
    // paramsList = paramsList.append('password', password);
    return this.http.get<User>(`${this.url + 'login'}`);
  }

}
