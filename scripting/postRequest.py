import requests
r = requests.post("http://web-scale.cloud:5000/addFood", data={"name":"celery","water usage (l/g)":30.0,"vegetarian":"vegan","kind":"vegetable","nutrition":10.76,"fat":0.5,"sodium":0.00001,"sugar":0.044,"carbs":0.22,"protein":0.21,"cholesterol":0.0})
print(r.status_code, r.reason)


r = requests.post("http://web-scale.cloud:5000/addRecipe", data={"name":"vegetable soup","celery":50,"carrot":60,"potato":20,"onion":10,"dry pasta":50,"palmoil":5})
print(r.status_code, r.reason)
