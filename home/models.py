from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    

class Product_Car(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reviews = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    description = models.TextField()
    automatic = models.BooleanField(default=True)
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





