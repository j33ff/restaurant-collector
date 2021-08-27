from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('about/', views.about, name='about'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/<int:restaurant_id>/', views.restaurants_detail, name="detail"),
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create'),
    path('restaurants/<int:pk>/update/', views.RestaurantUpdate.as_view(), name='restaurants_update'),
    path('restaurants/<int:pk>/delete/', views.RestaurantDelete.as_view(), name='restaurants_delete'),
    path('restaurants/<int:restaurant_id>/add_reservation/', views.add_reservation, name='add_reservation'),
    path('restaurants/<int:restaurant_id>/assoc_dish/<int:dish_id>/', views.assoc_dish, name='assoc_dish'),
    path('dishes/', views.DishList.as_view(), name='dishes_index'),
    path('dishes/<int:pk>/', views.DishDetail.as_view(), name='dishes_detail'),
    path('dishes/create/', views.DishCreate.as_view(), name='dishes_create'),
    path('dishes/<int:pk>/update/', views.DishUpdate.as_view(), name='dishes_update'),
    path('dishes/<int:pk>/delete/', views.DishDelete.as_view(), name='dishes_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]