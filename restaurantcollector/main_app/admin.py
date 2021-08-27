from django.contrib import admin
from .models import Restaurant, Reservation, Dish

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Reservation)
admin.site.register(Dish)