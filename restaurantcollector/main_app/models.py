from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

SEATS = (
    ('I', 'Inside'),
    ('P', 'Patio')
)

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('dishes_detail', kwargs={'pk': self.id})

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    stars = models.IntegerField()
    dishes = models.ManyToManyField(Dish)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'restaurant_id': self.id})

class Reservation(models.Model):
    date = models.DateField('Reservation Date')
    time = models.TimeField(auto_now=False, auto_now_add=False)
    seating = models.CharField(
        max_length=1,
        choices=SEATS,
        default=SEATS[0][0]   
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_seating_display()} on {self.date}"
    class Meta:
        ordering = ['-date']


