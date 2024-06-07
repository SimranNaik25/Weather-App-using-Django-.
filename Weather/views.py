
from django.shortcuts import render
import requests
from datetime import datetime

def home(request):
    weather_data = None
    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather_data(city)
    return render(request, 'weather/home.html', {'weather_data': weather_data})

def get_weather_data(city):
    api_key = 'ee9f8cf325814bcd0dc92f3f85bc0ce7'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed'],
            'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S'),
            'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S'),
        }
    else:
        weather_data = {'error': 'City not found'}
    return weather_data


