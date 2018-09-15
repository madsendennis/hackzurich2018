import { Component, OnInit } from '@angular/core';
import { Recipe } from '../recipe';
import { RECIPES} from '../mock-recipes'
import { RecipeRecommendation } from '../reciperecommendations';
import { RECIPE_RECOMMENDATIONS } from '../mock-recipe-recommendations'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  recipes : Recipe[] = RECIPES;
  selectedRecipe : Recipe;
  recipeResourceConsumption: number;
  recipeRecommendations : RecipeRecommendation[] = RECIPE_RECOMMENDATIONS;
  showRecipeRecommendations : boolean = false;

  constructor() { }

  ngOnInit() {
  }

  onSelect(recipeId: number): void {
    this.selectedRecipe = this.recipes.find(s => s.id == recipeId);
    this.recipeResourceConsumption = 0;
    this.selectedRecipe.ingredients.forEach(i => this.recipeResourceConsumption += i.resourceConsumption);
  }

  onViewRecommendations() {
    this.showRecipeRecommendations = true;
  }

  onHideRecommendations() {
    this.showRecipeRecommendations = false;
  }

  onShowIngredientsOfRecommendedRecipe(recommendationRecipeId: number) {
    this.recipeRecommendations.forEach(r => {
      if (recommendationRecipeId == r.recipeId) {
        r.showIngredients = true;
      } else {
        r.showIngredients = false;
      }
    });
  }
}
