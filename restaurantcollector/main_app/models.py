from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    stars = models.IntegerField()
    def __str__(self):
        return self.name


