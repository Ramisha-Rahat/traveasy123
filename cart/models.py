from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    driver_license = models.CharField(max_length=300)
    cnic = models.CharField(max_length=15)
    start_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    car_name = models.CharField(max_length=200)
    car_company = models.CharField(max_length=200)
    car_image = models.CharField(max_length=500) 
    car_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.car_name}"