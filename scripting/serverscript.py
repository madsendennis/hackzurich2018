from flask import Flask
import json
import pandas as pd

app = Flask(__name__)

def hello_world():
    return 'Hello, World!'


@app.route('/')
def forRufus():
	foodfile = "/home/patrick/Documents/hackzurich2018/hackzurich2018/data/food.xls"
	recipesfile = "/home/patrick/Documents/hackzurich2018/hackzurich2018/data/recipes_done.xls"
	fooddf = pd.read_excel(foodfile)
	fooddf = fooddf.dropna(how='all')
	fooddf = fooddf.set_index("Name")

	recipesdf = pd.read_excel(recipesfile)
	ingredientsdf = recipesdf.iloc[:,:len(fooddf)]
	recipelist = {}
	recipesjsonlist = []
	for col in ingredientsdf.iterrows():
	    counter = 0
	    ingrlist = []
	    for x in col[1]:
	        if x != 0:
	            ingrlist.append({"name":col[1].index[counter],"qty":x,"waterconsumption":(fooddf.loc[col[1].index[counter]]["Water Usage (L/g)"]*x)})
	        counter+=1
	    recipelist.update({col[0]:ingrlist})
	(recipelist)
	blub = list(zip(list(range(len(recipesdf))),list(recipesdf.index)))

	for line in blub:
	    recipesjsonlist.append({"id":line[0],"name":line[1],"ingredients":recipelist[line[1]],"nutrition":recipesdf.loc[line[1]]["Nutrition"],"fat":recipesdf.loc[line[1]]["Fat"],"sodium":recipesdf.loc[line[1]]["Sodium"],"sugar":recipesdf.loc[line[1]]["Sugar"],"carbs":recipesdf.loc[line[1]]["Carbs"],"protein":recipesdf.loc[line[1]]["Protein"],"cholesterol":recipesdf.loc[line[1]]["Cholesterol"],"vegetarian":recipesdf.loc[line[1]]["Vegetarian"],"kind":recipesdf.loc[line[1]]["Kind"]})

	recipesjsonlist
	jsonforrufus = json.dumps(recipesjsonlist)
	json.loads(jsonforrufus)
	return jsonforrufus