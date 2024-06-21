from django.urls import path
from .import views

urlpatterns = [
    path('', views.cart,name='cart' ),
    path('success/', views.success, name='success'), 
    path('accept/<int:booking_id>/', views.accept_booking, name='accept_booking'),
    path('reject/<int:booking_id>/', views.reject_booking, name='reject_booking'),
]