import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
from functools import cmp_to_key
import numpy as np

def readFoodStuff():
    features = pd.ExcelFile('../data/foodstest.xls')
    foods = features.parse(features.sheet_names[0]).fillna(0).values
    return foods


def orderFoods(selected, lib):
    sel = selected[1:-1]
    num,_ = lib.shape
    dist = []
    for item in lib:
        tocmp = item[1:-1]
        dist.append(euclidean_distances([sel], [tocmp])[0][0])
    dist = np.array(dist)[:,None]
    newlib = np.append(lib, dist, axis=1)
    return newlib[newlib[:, -1].argsort()]


def doSomeStuff():
    foodLib = readFoodStuff()
    select = foodLib[4,:]
    food = orderFoods(select, foodLib)
    print("Selected\n", select)
    for x in food:
        print(x)



if __name__ == '__main__':
    doSomeStuff()