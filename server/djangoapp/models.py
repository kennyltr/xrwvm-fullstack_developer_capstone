from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=[('SEDAN', 'Sedan'),
                                                    ('SUV', 'SUV'),
                                                    ('WAGON', 'Wagon')])
    year = models.IntegerField(default=2024, 
                               validators=[MaxValueValidator(1885), 
                                           MinValueValidator(9999)])
    
    def __str__(self):
        return self.name
