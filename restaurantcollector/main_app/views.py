from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Reservation, Restaurant, Dish
from .forms import ReservationForm
from datetime import date, time, datetime
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')

@login_required
def restaurants_index(request):
  restaurants = Restaurant.objects.filter(user=request.user)
  return render(request, 'restaurants/index.html', { 'restaurants': restaurants })

@login_required
def restaurants_detail(request, restaurant_id):
  restaurant = Restaurant.objects.get(id=restaurant_id)
  # Get the dishes the restaurant doesn't have
  dishes_restaurant_doesnt_have = Dish.objects.exclude(id__in = restaurant.dishes.all().values_list('id'))
  reservation_form = ReservationForm()
  return render(request, 'restaurants/detail.html', { 
    'restaurant': restaurant, 'reservation_form': reservation_form,
    'dishes': dishes_restaurant_doesnt_have  
  })

@login_required
def assoc_dish(request, restaurant_id, dish_id):
  # Note that you can pass a dish's id instead of the whole object
  Restaurant.objects.get(id=restaurant_id).dishes.add(dish_id)
  return redirect('detail', restaurant_id=restaurant_id)


#   print(request.POST['time'])
#   time = request.POST['time']
#   hours = int(time.slice(0, time.index(':')))
  
#   reservation_object = {
#     'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
#     'date': date.fromisoformat(request.POST['date']), 
#     'time': datetime.strptime(format_time, '%H:%M'),
#     'seating': request.POST['seating']
#   }
#   print("This is ", reservation_object)
  
@login_required
def add_reservation(request, restaurant_id):
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

@login_required
def delete_reservation(request, restaurant_id, reservation_id):
    Reservation.objects.filter(id=reservation_id).delete()
    return redirect('detail', restaurant_id=restaurant_id)

class RestaurantCreate(LoginRequiredMixin, CreateView):
  model = Restaurant
  fields = '__all__'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the restaurant
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class RestaurantUpdate(LoginRequiredMixin, UpdateView):
  model = Restaurant
  fields = ['cuisine', 'description', 'city','country','stars']

class RestaurantDelete(LoginRequiredMixin, DeleteView):
  model = Restaurant
  success_url = '/restaurants/'

class DishList(LoginRequiredMixin, ListView):
  model = Dish

class DishDetail(LoginRequiredMixin, DetailView):
  model = Dish

class DishCreate(LoginRequiredMixin, CreateView):
  model = Dish
  fields = '__all__'

class DishUpdate(LoginRequiredMixin, UpdateView):
  model = Dish
  fields = ['name', 'description']

class DishDelete(LoginRequiredMixin, DeleteView):
  model = Dish
  success_url = '/dishes/' 
