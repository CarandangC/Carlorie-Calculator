import requests
import json

response = requests.get("https://api.edamam.com/api/nutrition-data?app_id=01c34358&app_key=ffa99955fc303afb3d0204291d44c164&nutrition-type=cooking&ingr=100g%20rice")
app_id = "01c34358"
app_key = "ffa99955fc303afb3d0204291d44c164"

while True:
    food = input("Enter a food (or 'quit' to exit): ")
    if food == 'quit':
        break
    encoded_food = food.replace(" ", "%")
    url = f"https://api.edamam.com/api/nutrition-data?app_id={app_id}&app_key={app_key}&nutrition-type=cooking&ingr={encoded_food}"
    response =  requests.get(url)
    print(response.status_code)
    #gets the data from the api call
    data = response.json()
    calories = data["calories"]
    print(food + " calories: " + str(calories))
    #print(response.json())  