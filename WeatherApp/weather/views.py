import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
from django.http import HttpResponse

# Create your views here.


def home(request):
    appid = '#' #HERE PROVIDE API_CODE
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    all_cities = []

    cities = City.objects.all()

    if request.method == "POST":
        try:
            form = CityForm(request.POST)
            # i need to check here weather citi is available on the web-page
            if form.is_valid:
                form.save()

        except:
            return redirect('error')

    form = CityForm()

    for city in cities:
        res = requests.get(url.format(city.name)).json()

        # print(res)
        try:
            city_info = {
                'id': city.id,
                'city': city.name,
                'temp': res["main"]["temp"],
                'feels_like': res["main"]["feels_like"],
                'humidity': res["main"]["humidity"],
                'icon': res["weather"][0]["icon"]}

            all_cities.append(city_info)

        except:
            City.objects.filter(name=city).delete()
            return redirect('error')

    print(all_cities)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/home.html', context)


def error(request):

    return render(request, 'weather/error.html')


def deleteCity(request, pk):
    city = City.objects.get(name=pk)  

    if request.method == "POST":
        # print(city)
        city.delete()
        return redirect('home')

    return render(request, 'weather/delete.html')

