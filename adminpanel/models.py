from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
from home.models import Customer
from home.models import Product_Car

class Car(models.Model):
    CATEGORY_CHOICES = [
        ('Hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Pickup', 'Pickup'),
    ]

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    daily_rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    reviews = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    company = models.CharField(max_length=100, default='Unknown')
    fuel_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

#models

class AdminUsers(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def _str_(self):
        return self.username