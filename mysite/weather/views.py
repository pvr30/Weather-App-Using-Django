from django.shortcuts import render
import requests
import json
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        source_url = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+
                                city + '&units=metric&appid=c46d92ceb9e9b915470ab45fc26226b8')

        list_of_data = source_url.json()
        #print(list_of_data)
        data = {
            "country_code": list_of_data['sys']['country'],
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        #print(data)
    else:
        data = {}

    return render(request, "index.html", data)