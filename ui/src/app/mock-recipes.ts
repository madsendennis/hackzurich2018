import { Recipe } from "./recipe";

export const RECIPES : Recipe[] = [
    {id: 1, name: 'Recipe 1', ingredients : [
        {name: 'Ingredient 1', qty: 2, resourceConsumption: 3},
        {name: 'Ingredient 4', qty: 0.5, resourceConsumption: 4},
        {name: 'Ingredient 5', qty: 0.75, resourceConsumption: 0.5},
    ],
    resourceConsumption: 7.5 },
    {id: 2, name: 'Recipe 2', ingredients : [
        {name: 'Ingredient 4', qty: 0.5, resourceConsumption: 4},
        {name: 'Ingredient 5', qty: 0.75, resourceConsumption: 0.5},
    ],
    resourceConsumption: 4.5 },
    {id: 3, name: 'Recipe 3', ingredients : [
        {name: 'Ingredient 1', qty: 2, resourceConsumption: 3},
        {name: 'Ingredient 2', qty: 1, resourceConsumption: 5},
    ],
    resourceConsumption: 8 },
    {id: 4, name: 'Recipe 4', ingredients : [
        {name: 'Ingredient 2', qty: 1, resourceConsumption: 5},
        {name: 'Ingredient 3', qty: 1.5, resourceConsumption: 1},
        {name: 'Ingredient 5', qty: 0.75, resourceConsumption: 0.5},
    ],
    resourceConsumption: 6.5 },
] 