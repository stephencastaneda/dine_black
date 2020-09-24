import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dineblackapp.models import Restaurant, RestaurantDishReview
from ..connection import Connection

def get_restaurant(restaurant_id):

    all_restaurants = Restaurant.objects.get(pk=restaurant_id)

    return(all_restaurants)

def get_checkins(restaurant_id, restaurant):

    all_checkins = RestaurantDishReview.objects.all(restaurant_id=restaurant.id)

    return(all_checkins)

def restaurant_details(request, restaurant_id):
  if request.method == 'GET':
    restaurant = get_restaurant(restaurant_id)
    checkins = get_checkins(restaurant_id, restaurant)

    template = 'restaurants/detail.html'
    context = {
      'restaurant': restaurant,
      'checkins': checkins
    }

    return render(request, template, context)