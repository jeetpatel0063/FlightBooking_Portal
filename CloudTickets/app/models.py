from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Flight(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
