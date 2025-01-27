from django.db import models

# Create your models here.
class Car(models.Model):  
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)  
    year = models.PositiveIntegerField()  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    color = models.CharField(max_length=30)  
    mileage = models.PositiveIntegerField()  
    is_new = models.BooleanField(default=True) 
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"