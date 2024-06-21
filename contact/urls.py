from django.urls import path
from contact.views import *




urlpatterns = [
    path('contact/',contact, name = 'Contact'),
    path('saveContact/', savecontact,name='saveContact')
]

