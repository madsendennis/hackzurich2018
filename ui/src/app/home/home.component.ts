import { Component, OnInit } from '@angular/core';
import { Recipe } from '../recipe';
import { RecipeRecommendation } from '../reciperecommendations';
import { RECIPE_RECOMMENDATIONS } from '../mock-recipe-recommendations'
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_IPADDRESS } from '../custom.constants';
import { RecipeIngredient } from '../recipeingredient';
import { ApiJsonResponse } from '../api.json.response';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
@Injectable()
export class HomeComponent implements OnInit {
  recipes : Recipe[];
  selectedRecipe : Recipe;
  updatedRecipe : Recipe;
  isSelectedRecipeUpdated: boolean = false;
  recipeRecommendations : RecipeRecommendation[] = RECIPE_RECOMMENDATIONS;
  showRecipeRecommendations : boolean = false;
  showRecipes : boolean = false;
  alternateIngredients : RecipeIngredient[];
  alternateIngredientsDisplayedFor : string;

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

    this.selectedRecipe.resourceConsumption = 0;
    this.selectedRecipe.ingredients.forEach(i => {
      this.selectedRecipe.resourceConsumption += i.resourceConsumption;
    });

    this.updatedRecipe = this.onGetCopyOfSelectedRecipe();
    this.isSelectedRecipeUpdated = false;
    this.onHideRecipes();
  }

  onGetCopyOfSelectedRecipe(): Recipe {
    let copyRecipe : Recipe = new Recipe();
    copyRecipe.name = this.selectedRecipe.name;
    copyRecipe.resourceConsumption = this.selectedRecipe.resourceConsumption;
    copyRecipe.ingredients = [];
    this.selectedRecipe.ingredients.forEach(i => {
      let recipeIngredient = new RecipeIngredient();
      recipeIngredient.name = i.name;
      recipeIngredient.qty = i.qty;
      recipeIngredient.resourceConsumption = i.resourceConsumption;
      copyRecipe.ingredients.push(recipeIngredient);
    }); 

    copyRecipe.resourceConsumption = 0;
    copyRecipe.ingredients.forEach(i => {
      copyRecipe.resourceConsumption += i.resourceConsumption;
    });

    return copyRecipe;
  }

  onSwapIngredientsInRecipe(outIngredient: RecipeIngredient, inIngredient: RecipeIngredient) {
    let indexOfOutIngredient: number = this.updatedRecipe.ingredients.map(i => i.name).indexOf(outIngredient.name);
    this.updatedRecipe.ingredients[indexOfOutIngredient].name = inIngredient.name;
    this.updatedRecipe.ingredients[indexOfOutIngredient].qty = inIngredient.qty;
    this.updatedRecipe.ingredients[indexOfOutIngredient].resourceConsumption = inIngredient.resourceConsumption;
    this.alternateIngredients = null;
    this.updatedRecipe.resourceConsumption = 0;
    this.updatedRecipe.ingredients.forEach(i => {
      this.updatedRecipe.resourceConsumption += i.resourceConsumption;
    });
    this.isSelectedRecipeUpdated = true;
  }

  onViewRecommendations() {
    this.showRecipeRecommendations = true;
  }

  onHideRecommendations() {
    this.showRecipeRecommendations = false;
  }

  onShowIngredientsOfRecommendedRecipe(recommendation: RecipeRecommendation) {
    this.recipeRecommendations.forEach(r => {
      if (r.recipe.name == recommendation.recipe.name) {
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

  onShowAlternateIngredients(recipeIngredient: RecipeIngredient) {
    this.http.get(API_IPADDRESS + "/similarfoods?name=" + recipeIngredient.name + "&qty=" + recipeIngredient.qty).subscribe((data: RecipeIngredient[]) => {
      this.alternateIngredients = data;
      this.alternateIngredientsDisplayedFor = recipeIngredient.name;
    });
  }

  onHideAlternateIngredients() {
    this.alternateIngredients = null;
  }

  onConsumeFood(recipe: Recipe) {
    if (this.isSelectedRecipeUpdated) {
      recipe.name += "_*";
    }
    this.http.get(API_IPADDRESS + "/user/consumefood?name=" + recipe.name + "&resource=" + recipe.resourceConsumption).subscribe((data: ApiJsonResponse) => {
      if (data.isAdded) {
        this.selectedRecipe = null;
        this.updatedRecipe = null;
      }
    });
  }
}
