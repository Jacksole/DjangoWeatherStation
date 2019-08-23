import requests
from django.shortcuts import render

# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=25f038ac660853967450c1fdd96aa483'
    city = 'Las Vegas'
    # request the API data and convert the JSON to Python data types
    city_weather = requests.get(url.format(city)).json()

    # returns the index.html template
    return render(request, 'weather/index.html')
