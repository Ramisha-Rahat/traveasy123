'''app url'''
from django.urls import path
from .import views 

urlpatterns = [
path('', views.blog,name='blog' ),
path('pricing/', views.pricing, name='pricing' ),
path('terms/', views.terms, name='terms' )
]