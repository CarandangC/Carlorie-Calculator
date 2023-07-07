from flask import Flask, render_template, request
import requests

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nutrition', methods=['POST'])
def get_nutrition():
    app_id = "01c34358"
    app_key = "ffa99955fc303afb3d0204291d44c164"

    food = request.form.get('food')
    encoded_food = food.replace(" ", "%")
    url = f"https://api.edamam.com/api/nutrition-data?app_id={app_id}&app_key={app_key}&nutrition-type=cooking&ingr={encoded_food}"
    response = requests.get(url)

    #if the response is valid: return the nutritional value
    if response.status_code == 200:
        data = response.json()
        calories = data["calories"]
        print(response.json())
        return render_template('nutrition.html', food = food, calories = calories)
    
    else:
        return render_template('nutrition.html', error='Unable to fetch nutrition information')

if __name__ == '__main__':
    app.run(debug=True)
