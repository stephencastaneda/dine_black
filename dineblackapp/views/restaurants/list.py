import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dineblackapp.models import Restaurant, RestaurantDishReview
from ..connection import Connection

# def get_checkins(restaurant_id, restaurant):

#     all_checkins = RestaurantDishReview.objects.filter(restaurant_id=restaurant.id)
#     return(all_checkins)

def restaurant_list(request):
    if request.method == "GET":
    
        all_restaurants = Restaurant.objects.all()
        all_checkins = RestaurantDishReview.objects.all().values('restaurant_id').distinct()

        print(all_checkins)
        
        template_name = 'restaurants/list.html'

        context = {
            'all_restaurants': all_restaurants,
            'all_checkins': all_checkins
        }

        return render(request, template_name, context)

