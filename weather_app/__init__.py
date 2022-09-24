import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
3
app = Flask(__name__)
db = SQLAlchemy()


url = "http://api.openweathermap.org/data/2.5/weather?q={}&units+imperial&&appid=eb33b9299fdaf865b24df40ad97c627e"
city = "Nairobi"



r = requests.get(url.format(city)).json()
print(r)

@app.route('/')
def index():
    return render_template('weather.html')
