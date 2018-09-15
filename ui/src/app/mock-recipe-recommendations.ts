import { RecipeRecommendation } from "./reciperecommendations";

export const RECIPE_RECOMMENDATIONS : RecipeRecommendation[] = [
    {
        recipeId: 1,
        recipe: {id: 1, name: 'Recipe 1', ingredients : [
            {name: 'Ingredient 1', qty: 2, resourceConsumption: 3},
            {name: 'Ingredient 4', qty: 0.5, resourceConsumption: 4},
            {name: 'Ingredient 5', qty: 0.75, resourceConsumption: 0.5},
        ] },
        showIngredients: false
    },
    {
        recipeId: 2,
        recipe: {id: 2, name: 'Recipe 2', ingredients : [
            {name: 'Ingredient 4', qty: 0.5, resourceConsumption: 4},
            {name: 'Ingredient 5', qty: 0.75, resourceConsumption: 0.5},
        ] },
        showIngredients: false
    },
] 