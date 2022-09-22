import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

City_API_endpoint = "http://api.openweathermap.org/data/2.5/weather?q="
City = "Nairobi"
Country = ",KE,"
join_key = "&appid=" + "eb33b9299fdaf865b24df40ad97c627e"
units = "&units=metric"

current_city_weather = City_API_endpoint + City + Country + join_key + units
print(current_city_weather)

@app.route('/')
def index():
    return render_template('weather.html')
