import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dineblackapp.models import Restaurant
from ..connection import Connection

def get_restaurant(restaurant_id):

    all_restaurants = Restaurant.objects.get(pk=restaurant_id)

    return(all_restaurants)


def restaurant_details(request, restaurant_id):
  if request.method == 'GET':
    restaurant = get_restaurant(restaurant_id)

    template = 'restaurants/detail.html'
    context = {
      'restaurant': restaurant
    }

    return render(request, template, context)