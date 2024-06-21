from django.urls import path
from .views import car_submission_view

urlpatterns = [
    path('submission/', car_submission_view, name='submit_car'),
]