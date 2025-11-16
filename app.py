
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '689632bd623cdeb9b9b20f27219a64a2'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city', '').strip()

        if city == "":
            error = "Please enter a valid city name."
            return render_template('index.html', weather_data=None, error=error)

        # Build API URL
        url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

        # Call API
        response = requests.get(url)
        data = response.json()

        # If city is invalid
        if data.get('cod') != 200:
            error = "City not found. Please try again!"
        else:
            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].capitalize(),
                'icon': data['weather'][0]['icon']
            }

    return render_template('index.html', weather_data=weather_data, error=error)


if __name__ == '__main__':
    app.run(debug=True)
