from django.shortcuts import render
import requests
def index(request):
    api = "http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
    city = "kuwait"
    url = api + city
    response = requests.get(url)
    content = response.json()
    we = {
        'city':city,
        'temp': content['main']['temp'],
        'des':content['weather'][0]['description'],
        'icon':content['weather'][0]['icon']
    }
    return render(request,'weather.html',we)