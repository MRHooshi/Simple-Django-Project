from django.db import models
from restaurants.models import Restaurant


class Food(models.Model):
    name = models.CharField(max_length=25)
    price = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='foods')
