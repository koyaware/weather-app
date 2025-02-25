import requests
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import City
from .forms import CityForm


def remove_city(request: WSGIRequest, city_name):
    city_name = city_name.capitalize()
    try:
        City.objects.filter(name=city_name).delete()
        return redirect('home')
    except City.DoesNotExist:
        return HttpResponseNotFound('Город не найден в базе данных.')


def home(request: WSGIRequest) -> HttpResponse:
    appid = 'ВАШ АПИ'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:

        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res["weather"][0]['icon'],
            'temp_min': res['main']['temp_min'],
            'temp_max': res['main']['temp_max']
        }

        if not city_info in all_cities:
            all_cities.append(city_info)


    return render(
        request,
        'core/pages/index.html',
        context={
            'title': 'Главная страница',
            'all_info': all_cities,
            'form': form,
            'info_header': 'Информация'
        }
    )


def info(request: WSGIRequest) -> HttpResponse:

    appid = 'ВАШ АПИ'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:

        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res["weather"][0]['icon'],
            'temp_min': res['main']['temp_min'],
            'temp_max': res['main']['temp_max']
        }

        if not city.name in all_cities:
            all_cities.append(city_info)

    return render(
        request,
        'core/pages/info.html',
        context={
            'title': 'Главная страница',
            'all_info': all_cities,
            'form': form,
            'info_header': 'Главная'
        }
    )