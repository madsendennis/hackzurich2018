import pandas as pd
from sklearn.metrics.pairwise import cosine_distances
import numpy as np
import json

vegetarianDict = {"vegan": 0, "vegetarian": 1, "non-vegetarian": 2}


class getMaData:
    df = None
    def __init__(self, path):
        self.df   = pd.read_excel(path).fillna(0)
        self.len  = len(self.df)
        # self.dict = self.df.to_json(orient='records')

    def columnStringReplacementWithInt(self, columnName, replacementdict):
        self.df = self.df.replace({columnName: replacementdict})

    def getItem(self, name):
        return self.df.loc[self.df['name'] == name]

    def removeColumn(self, columnName):
        self.df = self.df.drop([columnName], axis=1)

    def dropStuffBeforeComparison(self, tmpdf):
        dropItems = ['water usage (l/g)', 'kind', 'energy consumption (mj/kg)', 'global warming potential (gwp) – kg of co2 / kg']
        for item in dropItems:
            tmpdf = tmpdf.drop([item], axis=1)
        return tmpdf

    def addSortingColumn(self, lentoName):
        similarity = 'similarity'
        dist = []
        startIndex = 1
        endIndex = -1
        sel = self.dropStuffBeforeComparison(self.getItem(lentoName)).values[0][startIndex:endIndex]
        for index, row in self.dropStuffBeforeComparison(self.df).iterrows():
            tocmp = row.values[startIndex:endIndex]
            dist.append(cosine_distances([sel], [tocmp])[0][0])
        self.df[similarity] = dist
        self.df = self.df.sort_values(similarity, ascending=True)

    def getMostSimilar(self, name, threshold=0):
        self.addSortingColumn(name)
        #should be less than th + remove if 0.0
        # return self.df['similarity'] < 50
        return self.df[1:4]





def cleanForShowingRecipe(locdf, numOfFoodItems):
    locdf = locdf.set_index("name")
    ingredientsdf = locdf.iloc[:,1:numOfFoodItems]
    recipesjsonlist = []
    for rows in ingredientsdf.iterrows():
        ingrlist = []
        for (counter, x) in enumerate(rows[1]):
            if x != 0:
                ingrlist.append({"name":rows[1].index[counter],"qty":x})
        recipesjsonlist.append({'name': rows[0], 'ingredients': ingrlist, 'showIngredients': False})
    return json.dumps(recipesjsonlist)


def prepareFood():
    obj = getMaData('../data/food.xls')
    # obj.removeColumn('kind')
    obj.columnStringReplacementWithInt('vegetarian', vegetarianDict)
    obj.addSortingColumn('cabbage')
    return obj

def prepareRecipe():
    obj = getMaData('../data/recipes_done.xls')
    # obj.removeColumn('kind')
    obj.columnStringReplacementWithInt('vegetarian', vegetarianDict)
    obj.addSortingColumn('mixed salad')
    return obj

if __name__ == '__main__':
    foodObj = prepareFood()
    reciObj = prepareRecipe()

    foods = foodObj.getMostSimilar('beef')
    recip = reciObj.getMostSimilar('meat pizza')

    hest = cleanForShowingRecipe(recip, foodObj.len)

    pass