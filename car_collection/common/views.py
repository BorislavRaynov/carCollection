from django.shortcuts import render
from car_collection.car.models import Car
# Create your views here.

def index(request):
    return render(request, 'car_collection/common/index.html')

def catalogue(request):
    cars = Car.objects.all()

    context = {
        'cars': cars
    }

    return render(request, 'car_collection/common/catalogue.html', context=context)
