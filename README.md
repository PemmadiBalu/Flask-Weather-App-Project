#🌦️ Flask Weather App

A simple and beautiful Flask web application that allows users to check real-time weather information using the OpenWeatherMap API.
This project is ideal for beginners learning Flask, HTML, CSS, APIs, and frontend styling.

#📂Features

Enter any city name to get live weather updates

Displays temperature, weather description, city & country

Weather icons (sun, rain, clouds, etc.)

Input validation (empty or wrong city name alerts)

Clean, modern UI with animations

Uses OpenWeatherMap API for weather data

#🛠️ Technologies Used

Backend: Python, Flask

API: OpenWeatherMap API

Frontend: HTML, CSS

Requests: Python requests library

Template Engine: Flask Jinja2

#⚡ Project Structure
flask-weather-app/
│
├── app.py                 # Main Flask application
│
├── static/
│   └── style.css          # CSS styles
│
└── templates/
    └── index.html         # Main UI page

#🚀 Installation
1. Clone the repository
git clone https://github.com/yourusername/flask-weather-app.git
cd flask-weather-app

2. Install dependencies
pip install flask requests

3. Add your OpenWeatherMap API key

#Inside app.py, update:

API_KEY = "YOUR_API_KEY_HERE"


Get free key from: https://openweathermap.org/

4. Run the application
python app.py

5. Open in browser
http://127.0.0.1:5000/
