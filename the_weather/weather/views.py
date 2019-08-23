import requests
from django.shortcuts import render

# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b3c56501c723bf75c4b4474353af7545'
    city = 'Las Vegas'
    # request the API data and convert the JSON to Python data types
    city_weather = requests.get(url.format(city)).json()
    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }
    context = {'weather': weather}
    # returns the index.html template
    return render(request, 'weather/index.html')
