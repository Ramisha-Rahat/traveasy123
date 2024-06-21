'''2nd app url'''
from django.urls import path
from .import views 

urlpatterns = [
     path('', views.dashboard, name='adminpanel'),
     path('login/', views.custom_admin_login, name='custom_admin_login'),
]