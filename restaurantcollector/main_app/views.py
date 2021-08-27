from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Restaurant, Dish
from .forms import ReservationForm
import datetime

# Create your views here.


def home(request):
    return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
def restaurants_index(request):
  restaurants = Restaurant.objects.all()
  return render(request, 'restaurants/index.html', { 'restaurants': restaurants })
def restaurants_detail(request, restaurant_id):
  restaurant = Restaurant.objects.get(id=restaurant_id)
  # Get the dishes the restaurant doesn't have
  dishes_restaurant_doesnt_have = Dish.objects.exclude(id__in = restaurant.dishes.all().values_list('id'))
  reservation_form = ReservationForm()
  return render(request, 'restaurants/detail.html', { 
    'restaurant': restaurant, 'reservation_form': reservation_form,
    'dishes': dishes_restaurant_doesnt_have  
  })

def assoc_dish(request, restaurant_id, dish_id):
  # Note that you can pass a dish's id instead of the whole object
  Restaurant.objects.get(id=restaurant_id).dishes.add(dish_id)
  return redirect('detail', restaurant_id=restaurant_id)

def add_reservation(request, restaurant_id):
  # print(request.POST['time'])
  # reservation_object = {
  #   'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'], 
  #   'time': datetime.time.strptime(request.POST['time'], '%H:%M'),
  #   'seating': request.POST['seating']
  # }
  #  datetime.time

  form = ReservationForm(request.POST)
  try:
    if form.is_valid():
      print("form is valid")
      new_reservation = form.save(commit=False)
      new_reservation.restaurant_id = restaurant_id
      new_reservation.save()
    return redirect('detail', restaurant_id=restaurant_id)
  except:
    print("form not valid")

class RestaurantCreate(CreateView):
  model = Restaurant
  fields = '__all__'
class RestaurantUpdate(UpdateView):
  model = Restaurant
  fields = ['cuisine', 'description', 'city','country','stars']
class RestaurantDelete(DeleteView):
  model = Restaurant
  success_url = '/restaurants/'

class DishList(ListView):
  model = Dish

class DishDetail(DetailView):
  model = Dish

class DishCreate(CreateView):
  model = Dish
  fields = '__all__'

class DishUpdate(UpdateView):
  model = Dish
  fields = ['name', 'description']

class DishDelete(DeleteView):
  model = Dish
  success_url = '/dishes/' 
