import { Component, OnInit } from '@angular/core';
import { Recipe } from '../recipe';
import { RECIPES} from '../mock-recipes'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  recipes : Recipe[] = RECIPES;

  constructor() { }

  ngOnInit() {
  }

}
