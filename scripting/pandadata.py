import pandas as pd
foodfile = "../data/food.xls"
recipesfile = "../data/recipes.xls"
fooddf = pd.read_excel(foodfile)
fooddf = fooddf.dropna(how='all')
fooddf = fooddf.set_index("Name")
#fooddf
recipesdf = pd.read_excel(recipesfile)
recipesdf = recipesdf.fillna(0)
#recipesdf
newcols = []
veglist=["Non-vegetarian","Vegetarian","Vegan"]
for cols in fooddf.columns[2:]:
    #print(cols)
    col = []
    for recipe in recipesdf.iterrows():
        nutrition = 0
        ifstring = []
        isstring = False
        for ingredient in range(len(recipe[1])):
            if(recipe[1][ingredient] != 0.0):
                if(type(fooddf.loc[recipesdf.columns[ingredient]][cols]) is str):
                    isstring = True
                    ifstring.append(fooddf.loc[recipesdf.columns[ingredient]][cols])
                else:
                    isstring = False
                    nutrition += recipe[1][ingredient]*fooddf.loc[recipesdf.columns[ingredient]][cols]     
        if(isstring):
            ifstring = set(ifstring)
            isveg = False
            for veg in veglist:
                if(veg in ifstring):
                    isveg = True
                    col.append(veg)
                    break
            if not isveg:
                col.append(set(ifstring))
        else:
            col.append(nutrition)
    #print(col)
    newcols.append(col)
    
for cols in range(len(fooddf.columns[2:])):
    recipesdf[fooddf.columns[2:][cols]] = newcols[cols]
recipesdf.to_excel("../data/recipes_done.xls")