import requests
from weather_app.models import City
from weather_app import db
from flask import Blueprint, jsonify, request, render_template

weather = Blueprint('weather', __name__)


@weather.route('/')
def index():

    cities = City.query.all()

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units+imperial&&appid=eb33b9299fdaf865b24df40ad97c627e"

    weather_data = []

    for city in cities:

      r = requests.get(url.format(city.name)).json()
      weather = {
          'city': city.name,
          'temperature': r['main']['temp'],
          'description': r['weather'][0]['description'],
          'icon': r['weather'][0]['icon'],
      }

      print(weather)

      weather_data.append(weather)

    return render_template('weather.html', weather_data=weather_data)


@weather.route('/city', methods=['POST'])
def create_city():
    data = request.get_json()

    new_city = City(name=data['name'])
    db.session.add(new_city)
    db.session.commit()

    return jsonify({"message": "New city created"})


@weather.route('/city', methods=['GET'])
def get_all_cities():
    cities = City.query.all()

    output = []

    for city in cities:

        city_data = {}
        city_data['name'] = city.name
        output.append(city_data)

    return jsonify({'cities': output})
