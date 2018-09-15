import pandas as pd
import numpy as np
import json
from sklearn.metrics.pairwise import euclidean_distances


class dataHandler:
    def __init__(self):
        # Load the files
        self.food    = pd.read_excel('../data/food.xls').fillna(0)
        self.foodFeatures = self.food[['Name','Nutrition', 'Fat', 'Sodium', 'Sugar', 'Carbs', 'Protein', 'Cholesterol']]
        # self.recipes = pd.read_excel('../data/food.xls').fillna(0)

    def foodGetAll(self):
        self.__foodjson = self.food.reset_index().to_json(orient='records')
        return self.__foodjson

    def foodCompare(self, itemId):
        sel = self.food.values[itemId][6:-1]
        dist = []
        for item in self.food.values:
            tocmp = item[6:-1]
            dist.append(euclidean_distances([sel], [tocmp])[0][0])
        dist = np.array(dist)[:, None]
        tmplib = np.append(self.food, dist, axis=1)
        return tmplib[tmplib[:, -1].argsort()]



if __name__ == '__main__':
    obj = dataHandler()

    somedata = obj.foodGetAll()

    parsed = json.loads(somedata)
    print(json.dumps(parsed, indent=4, sort_keys=True))
    cmp = obj.foodCompare(1)
    pass