import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.


def index(request):
    appid = '2972edf4bc2a4121567fb4a5e4e3188a'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid

    all_cities = []

    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm() # this line will clean up the city form and keep it empty after page is updated


    cities = City.objects.all()
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        print(res)

        city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"]}
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)


