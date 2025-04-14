import json
#Create a Json, in this case is a Dictionary
cars_json ='{"Brand":"Honda","Name":"Civic", "Color":"Black"}'

#Loads the Json
#cars = json.loads(cars_json)

#print(cars['Brand'])


#create a simple Dictionary
clothes= {"Brand":"Nike","Name":"Shirt","Color":"Black"}

#Convert de dictionary in a json
clothes_json = json.dumps(clothes,indent=3,sort_keys=True,separators=(':','='))

#print(clothes_json)

#import a json from other file
with open('C:/Users/erikv/Documents/repositorios GitHub/Python-Study/Jsonstudy/json1.json') as f:
    cars = json.load(f)

print(cars)