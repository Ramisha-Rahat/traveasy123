from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    products = Product_Car.objects.all()
    context = {'products':products}
    return render(request, 'home/home.html', context)

