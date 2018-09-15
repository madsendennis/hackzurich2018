import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
from functools import cmp_to_key


def readFoodStuff():
    features = pd.ExcelFile('../data/foods.xls')
    foods = features.parse(features.sheet_names[0]).fillna(0).values
    return foods


def orderFoods(selected, lib):
    print("Orig", selected)
    sel = selected[1:-1]
    num,_ = lib.shape
    for item in lib:
        tocmp = item[1:-1]
        dist = euclidean_distances([sel], [tocmp])
        print("DIST: ", dist[0][0], " ::: ", item)
    # print(dist)
    pass

def my_cmp(a, b):
    pass

def doSomeStuff():
    foods = readFoodStuff()
    orderFoods(foods[4,:], foods)
    # print(foods[0,:])

    # sorted(foods, key=cmp_to_key(compare_versions))
    # sorted(foods, key=cmp_to_key(greater))

if __name__ == '__main__':
    doSomeStuff()