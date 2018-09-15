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
  selectedRecipe : Recipe;
  recipeResourceConsumption: number;

  constructor() { }

  ngOnInit() {
  }

  onSelect(recipeId: number): void {
    this.selectedRecipe = this.recipes.find(s => s.id == recipeId);
    this.recipeResourceConsumption = 0;
    this.selectedRecipe.ingredients.forEach(i => this.recipeResourceConsumption += i.resourceConsumption);
  }
}
