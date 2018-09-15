import { Component, OnInit, Injectable } from '@angular/core';
import { Dashboard } from '../dashboard'
import { HttpClient } from '@angular/common/http';
import { API_IPADDRESS } from '../custom.constants';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
@Injectable()
export class DashboardComponent implements OnInit {
  overview: Dashboard;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.http.get(API_IPADDRESS + "/user/overview").subscribe((data: Dashboard) => {
      this.overview = data;
    });
  }

}
