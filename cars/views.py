from django.shortcuts import render
from .models import *

from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

# def cars(request):
#     car_type=Car.objects.all()
#     context={'car_type':car_type,}
#     return render(request, 'cars/car.html', context)

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car.html', {'car_type': cars})