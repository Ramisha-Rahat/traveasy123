from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from cars.models import Car
from cart.models import Booking
from user.models import UserCar
from contact.models import saveContact
from .forms import AdminLoginForm
from django.contrib import messages
from adminpanel.models import AdminUsers


def adminpanel(request):
    try:
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username).first()

            if not user_obj:
                messages.info(request, 'Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            user_obj = authenticate(username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('/dashboard/')
            
            messages.info(request, 'Invalid Password')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        return render(request, 'adminpanel/adminpanel.html')
    
    except Exception as e:
        print(e)
        # Optionally log the error
        messages.error(request, 'An error occurred during login.')
        return render(request, 'adminpanel/adminpanel.html') 
    

def dashboard(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CarForm()
    
    bookings = Booking.objects.all().order_by('-id')
    
    cars = UserCar.objects.all()

    responses=saveContact.objects.all()
    return render(request, 'adminpanel/dashboard.html', {'form': form, 'bookings': bookings,'cars': cars, 'responses':responses})

def custom_admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                admin_user = AdminUsers.objects.get(username=username, password=password)
                # Here you would typically set a session or token
                # For simplicity, we are just showing a success message
                messages.success(request, 'You have successfully logged in.')
                return redirect('adminpanel')  # Redirect to the admin panel
            except AdminUsers.DoesNotExist:
                messages.error(request, 'YOU ARE NOT ADMIN.')
    else:
        form = AdminLoginForm()
    
    return render(request, 'adminpanel/login.html', {'form': form})

