from django.db import models

class UserCar(models.Model):
    ENGINE_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric'),
    ]

    CATEGORY_CHOICES = [
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('Pickup', 'Pickup'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    cnic = models.CharField(max_length=15)
    car_name = models.CharField(max_length=100)
    car_company = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    car_description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    engine = models.CharField(max_length=10, choices=ENGINE_CHOICES)

    def __str__(self):
        return self.car_name

