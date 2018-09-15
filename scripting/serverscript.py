from flask import Flask
import json
import pandas as pd
import pandadata as pdt
from flask import request
from pandas.io.json import json_normalize


app = Flask(__name__)

def hello_world():
    return 'Hello, World!'


@app.route('/recipes')
def recipes():
	foodfile = "../data/food.xls"
	recipesfile = "../data/recipes_done.xls"
	fooddf = pd.read_excel(foodfile)
	fooddf = fooddf.dropna(how='all')
	fooddf = fooddf.set_index("name")

	recipesdf = pd.read_excel(recipesfile)
	recipesdf = recipesdf.set_index("name")
	ingredientsdf = recipesdf.iloc[:,:len(fooddf)]
	recipelist = {}
	recipesjsonlist = []
	for col in ingredientsdf.iterrows():
	    counter = 0
	    ingrlist = []
	    for x in col[1]:
	        if x != 0:
	            ingrlist.append({"name":col[1].index[counter],"qty":x,"waterconsumption":(fooddf.loc[col[1].index[counter]]["water usage (l/g)"]*x)})
	        counter+=1
	    recipelist.update({col[0]:ingrlist})
	(recipelist)
	blub = list(zip(list(range(len(recipesdf))),list(recipesdf.index)))

	for line in blub:
	    recipesjsonlist.append({"id":line[0],"name":line[1],"ingredients":recipelist[line[1]],"nutrition":recipesdf.loc[line[1]]["nutrition"],"fat":recipesdf.loc[line[1]]["fat"],"sodium":recipesdf.loc[line[1]]["sodium"],"sugar":recipesdf.loc[line[1]]["sugar"],"carbs":recipesdf.loc[line[1]]["carbs"],"protein":recipesdf.loc[line[1]]["protein"],"cholesterol":recipesdf.loc[line[1]]["cholesterol"],"vegetarian":recipesdf.loc[line[1]]["vegetarian"],"kind":recipesdf.loc[line[1]]["kind"]})

	recipesjsonlist
	jsonforrufus = json.dumps(recipesjsonlist)
	json.loads(jsonforrufus)
	return jsonforrufus

@app.route('/addFood', methods=["POST"])
def addFood():
	food = request.form.to_dict()
	pdt.addFood(food)
	return "hello world"

@app.route('/addRecipe', methods=["POST"])
def addRecipe():
	recipe = request.form.to_dict()
	pdt.addRecipe(recipe)
	return "hello world"
