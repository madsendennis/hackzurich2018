from flask import Flask
import json
import pandas as pd
import pandadata as pdt
from flask import request
from pandas.io.json import json_normalize
from newStuff import prepareRecipe, prepareFood, getMaData, cleanForShowingRecipe

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
    response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response
    
@app.route('/')
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
        ingrlist = []
        for (counter, x) in enumerate(col[1]):
            if x != 0:
                ingrlist.append({"name":col[1].index[counter],"qty":x,"waterconsumption":(fooddf.loc[col[1].index[counter]]["water usage (l/g)"]*x)})
        recipelist.update({col[0]:ingrlist})
    blub = list(zip(list(range(len(recipesdf))),list(recipesdf.index)))

    for line in blub:
        recipesjsonlist.append({"id":line[0],"name":line[1],"ingredients":recipelist[line[1]],"nutrition":recipesdf.loc[line[1]]["nutrition"],"fat":recipesdf.loc[line[1]]["fat"],"sodium":recipesdf.loc[line[1]]["sodium"],"sugar":recipesdf.loc[line[1]]["sugar"],"protein":recipesdf.loc[line[1]]["protein"],"vegetarian":recipesdf.loc[line[1]]["vegetarian"],"kind":recipesdf.loc[line[1]]["kind"],"carbs":recipesdf.loc[line[1]]["carbs"], "cholesterol":recipesdf.loc[line[1]]["cholesterol"]})

    jsonload = json.dumps(recipesjsonlist)
    json.loads(jsonload)
    return jsonload
    # return json.dumps({})

@app.route('/addFood', methods=["POST"])
def addFood():
    food = request.form.to_dict()
    pdt.addFood(food)
    return "{'isAdded':True}"

@app.route('/addRecipe', methods=["POST"])
def addRecipe():
    recipe = request.form.to_dict()
    pdt.addRecipe(recipe)
    return "{'isAdded':True}"

@app.route('/similarrecipes', methods=["GET"])
def similarRecipes():
    name = request.args.get('name')
    foodObj = prepareFood()
    reciObj = prepareRecipe()
    similar = reciObj.getMostSimilar(name)
    return json.dumps(cleanForShowingRecipe(similar, foodObj))

