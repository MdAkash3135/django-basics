from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Resturant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        ITALIAN = 'IT', 'Italian'
        MEXICAN = 'MX', 'Mexican'
        CHINESE = 'CH', 'Chinese'
        THAI = 'TH', 'Thai'
        JAPANESE = 'JP', 'Japanese'
    
    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitute = models.FloatField( validators=[
            MinValueValidator(-90),
            MaxValueValidator(90),
        ])
    resturant_type = models.CharField(max_length=2, choices=TypeChoices.choices)