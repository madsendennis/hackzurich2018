import pandas as pd

def readnwritenparse():
	foodfile = "../data/food.xls"
	recipesfile = "../data/recipes.xls"
	fooddf = pd.read_excel(foodfile)
	fooddf = fooddf.dropna(how='all')
	fooddf = fooddf.set_index("name")
	#fooddf
	recipesdf = pd.read_excel(recipesfile)
	recipesdf = recipesdf.fillna(0)
	recipesdf = recipesdf.set_index("name")
	#recipesdf
	newcols = []
	veglist=["non-vegetarian","vegetarian","vegan"]
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
	                    ifstring.extend((fooddf.loc[recipesdf.columns[ingredient]][cols]).replace(" ","").split(","))
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
	recipesdf.index.name="name"
	recipesdf.to_excel("../data/recipes_done.xls")

def addFood(food):
	foodfile = "../data/food.xls"
	fooddf = pd.read_excel(foodfile)
	fooddf = fooddf.dropna(how='all')
	fooddf = fooddf.set_index("name")
	recipesfile = "../data/recipes.xls"
	recipesdf = pd.read_excel(recipesfile)
	recipesdf = recipesdf.fillna(0)
	food = pd.DataFrame(food, index=[0])
	food = food.set_index("name")
	if(list(food.index)[0] not in list(fooddf.index)):
		print("added")
		fooddf = fooddf.append(food).fillna(0)
		fooddf = fooddf.drop_duplicates()
		fooddf.drop_duplicates().sort_index().to_excel("../data/food.xls")
		readnwritenparse()
	a = 1

def addRecipe(recipe):
	foodfile = "../data/food.xls"
	fooddf = pd.read_excel(foodfile)
	fooddf = fooddf.dropna(how='all')
	fooddf = fooddf.set_index("name")
	recipesfile = "../data/recipes.xls"
	recipesdf = pd.read_excel(recipesfile)
	recipesdf = recipesdf.fillna(0)
	recipesdf = recipesdf.set_index("name")

	recipe = pd.DataFrame(recipe, index=[0])
	recipe = recipe.set_index("name")
	if(recipe.index[0] not in list(recipesdf.index)):
		print("added")
		recipesdf = recipesdf.append(recipe).fillna(0)
		recipesdf.sort_index().to_excel("../data/recipes.xls")
		readnwritenparse()
	a = 1

readnwritenparse()
