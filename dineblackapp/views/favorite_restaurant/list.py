import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dineblackapp.models import FavoriteRestaurant, Diner, Restaurant
from ..connection import Connection

def get_restaurants():

        all_restaurants = Restaurant.objects.all()

        return(all_restaurants)


def favorite_list(request):
    if request.method == "GET":

        restaurants = get_restaurants()
        diner = Diner.objects.get(user=request.user)
        user_favorites = FavoriteRestaurant.objects.filter(diner=diner)
        template_name = 'favorite_restaurants/list.html'

        context = {
            'user_favorites': user_favorites,
            'restaurants': restaurants,
        }

        return render(request, template_name, context)

    elif request.method == 'POST':
        new_favorite = FavoriteRestaurant()
        new_favorite.diner = Diner.objects.get(user=request.user)
        new_favorite.restaurant = Restaurant.objects.get(pk=request.POST["restaurant"])   
        
        new_favorite.save()

        template_name = 'favorite_restaurants/list.html'

        context = {
          'new_favorite': new_favorite
        }

        return redirect(reverse('dineblackapp:favorites'))

    elif request.method == 'POST':
      form_data = request.POST

      if (
        "actual_method" in form_data
        and form_data["actual_method"] == "DELETE"
      ):

        favorite_restaurant_to_destroy = FavoriteRestaurant.objects.get(pk=favoriterestaurant_id)
        favorite_restaurant_to_destroy.delete()
            
        return redirect(reverse('dineblackapp:favorites'))