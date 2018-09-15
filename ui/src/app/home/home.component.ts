import { Component, OnInit } from '@angular/core';
import { Recipe } from '../recipe';
import { RecipeRecommendation } from '../reciperecommendations';
import { RECIPE_RECOMMENDATIONS } from '../mock-recipe-recommendations'
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_IPADDRESS } from '../custom.constants';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
@Injectable()
export class HomeComponent implements OnInit {
  recipes : Recipe[];
  selectedRecipe : Recipe;
  recipeRecommendations : RecipeRecommendation[] = RECIPE_RECOMMENDATIONS;
  showRecipeRecommendations : boolean = false;
  showRecipes : boolean = false;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.http.get(API_IPADDRESS + "/recipes").subscribe((data: Recipe[]) => {
      this.recipes = data;
    });
  }

  onSelect(recipe: Recipe): void {
    this.selectedRecipe = recipe;
    this.http.get(API_IPADDRESS + "/similarrecipes?name="+recipe.name).subscribe((data: RecipeRecommendation[]) => {
      this.recipeRecommendations = data;
    });
    this.onHideRecipes();
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

  onChoosingRecommendedRecipe(recommendedRecipe: RecipeRecommendation) {
    recommendedRecipe.showIngredients = false;
    this.onHideRecommendations();
    this.onSelect(recommendedRecipe.recipe);
  }

  onShowRecipes() {
    this.showRecipes = true;
  }

  onHideRecipes() {
    this.showRecipes = false;
  }
}
