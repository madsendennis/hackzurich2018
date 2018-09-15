from flask import Flask
import json
import pandas as pd
import pandadata as pdt
from flask import request
from pandas.io.json import json_normalize
from newStuff import prepareRecipe, prepareFood, getMaData, cleanForShowingRecipe, cleanForShowingFoods
from user import userHandler

userid = '0001'

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
                ingrlist.append({"name":col[1].index[counter],"qty":x,"resourceConsumption":round(fooddf.loc[col[1].index[counter]]["water usage (l/g)"]*x, 2)})
        recipelist.update({col[0]:ingrlist})
    blub = list(zip(list(range(len(recipesdf))),list(recipesdf.index)))

    for line in blub:
        recipesjsonlist.append({"id":line[0],"name":line[1],"ingredients":recipelist[line[1]],"nutrition":recipesdf.loc[line[1]]["nutrition"],"fat":recipesdf.loc[line[1]]["fat"],"sodium":recipesdf.loc[line[1]]["sodium"],"sugar":recipesdf.loc[line[1]]["sugar"],"protein":recipesdf.loc[line[1]]["protein"],"vegetarian":recipesdf.loc[line[1]]["vegetarian"],"kind":recipesdf.loc[line[1]]["kind"],"carbs":recipesdf.loc[line[1]]["carbs"], "cholesterol":recipesdf.loc[line[1]]["cholesterol"], "resourceConsumption": round(recipesdf.loc[line[1]]['water usage (l/g)'], 2)})

    jsonload = json.dumps(recipesjsonlist)
    json.loads(jsonload)
    return jsonload

@app.route('/addFood', methods=["POST"])
def addFood():
    food = request.form.to_dict()
    pdt.addFood(food)
    return json.dumps({'isAdded': True})

@app.route('/addRecipe', methods=["POST"])
def addRecipe():
    recipe = request.form.to_dict()
    pdt.addRecipe(recipe)
    return json.dumps({'isAdded': True})

@app.route('/similarrecipes', methods=["GET"])
def similarRecipes():
    name = request.args.get('name', None)
    foodObj = prepareFood()
    reciObj = prepareRecipe()
    similar = reciObj.getMostSimilar(name)
    return json.dumps(cleanForShowingRecipe(similar, foodObj))

@app.route('/similarfoods', methods=["GET"])
def similarFoods():
    name = request.args.get('name', None)
    qty = request.args.get('qty', None)
    foodObj = prepareFood()
    similar = foodObj.getMostSimilar(name)
    return json.dumps(cleanForShowingFoods(similar, qty))

@app.route('/user/consumefood', methods=["GET"])
def userConsumefood():
    user = userHandler(userid)
    name = request.args.get('name', None)
    resource = request.args.get('resource', None)
    user.addEntry(name, resource)
    return json.dumps({'isAdded':True})

@app.route('/user/overview')
def userOverview():
    user = userHandler(userid)
    return json.dumps({'today': round(user.getConsumptionDay()/1000.0,2), 'week': round(user.getConsumptionWeek()/1000.0,2), 'month': round(user.getConsumptionMonth()/1000.0,2), 'year': round(user.getConsumptionYear()/1000.0,2),
                       'thresholdToday': 3.5, 'thresholdWeek': 24.5, 'thresholdMonth': 105.0, 'thresholdYear':1277.5})

# 5000 L/day = 5kL
# week - 35L
# month - 150L
# year - 1825
