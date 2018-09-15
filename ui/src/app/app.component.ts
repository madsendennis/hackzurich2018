import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title : string = 'Sustainable Recipes';
  showHome : boolean = true;
  showAddRecipe : boolean = false;
  showDashboard : boolean = false;
  navbarOpen : boolean = false;

  onShowHome() {
    this.showHome = true;
    this.showAddRecipe = false;
    this.showDashboard = false;
    this.onNavbarToggle();
  }

  onShowDashboard() {
    this.showHome = false;
    this.showAddRecipe = false;
    this.showDashboard = true;
    this.onNavbarToggle();
  }

  onNavbarToggle() {
    if (this.navbarOpen) {
      this.navbarOpen = false;
    } else {
      this.navbarOpen = true;
    }
  }
}
