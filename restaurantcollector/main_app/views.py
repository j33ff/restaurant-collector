from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Restaurant:
    def __init__(self, name, cuisine, description, city, country, stars):
        self.name = name
        self.cuisine = cuisine
        self.description = description
        self.city = city
        self.country = country
        self.stars = stars

restaurants = [
    Restaurant('Minami', 'Japanese', 'Amazing Salmon Oshi','Vancouver', 'Canada', 5),
    Restaurant('Maenam', 'Thai', 'Delicious Steamed Local Clams','Vancouver', 'Canada', 4),
    Restaurant('Sing Sing','Fusion', 'Fantastic beer selection and pizza','Vancouver', 'Canada', 4),
]

def home(request):
    return HttpResponse('<h1>Restuarant Collector</h1>')
def about(request):
  return render(request, 'about.html')
def restaurants_index(request):
  return render(request, 'restaurants/index.html', { 'restaurants': restaurants })
