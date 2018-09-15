import {RecipeIngredient} from './recipeingredient'

export class Recipe {
    id: number;
    name: string;
    ingredients: RecipeIngredient[];
    resourceConsumption: number;
}