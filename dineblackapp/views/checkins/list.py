import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dineblackapp.models import RestaurantDishReview, Diner, Restaurant, RestaurantDishReview
from ..connection import Connection

def get_restaurants():

        all_restaurants = Restaurant.objects.all()

        return(all_restaurants)


def check_in_list(request):
    if request.method == "GET":

        restaurants = get_restaurants()
        diner = Diner.objects.get(user=request.user)
        user_check_ins = RestaurantDishReview.objects.filter(diner=diner)
        template_name = 'checkins/list.html'

        context = {
            'user_check_ins': user_check_ins,
            'restaurants': restaurants,
        }

        return render(request, template_name, context)

    elif request.method == 'POST':
        new_check_in = RestaurantDishReview()
        new_check_in.diner = Diner.objects.get(user=request.user)
        new_check_in.restaurant = Restaurant.objects.get(pk=request.POST["restaurant"])
        new_check_in.dish_name = request.POST["dish_name"]
        new_check_in.dish_img = request.POST["dish_image"]
        new_check_in.dish_rating_number = request.POST["dish_rating_number"]
        new_check_in.created_at = request.POST["created_at"]

        new_check_in.save()

        template_name = 'checkins/list.html'

        context = {
          'new_check_in': new_check_in
        }

        return redirect(reverse('dineblackapp:checkins'))

    elif request.method == 'POST':
      form_data = request.POST

      if (
        "actual_method" in form_data
        and form_data["actual_method"] == "DELETE"
      ):

        restaurant_review_to_burn = RestaurantDishReview.objects.get(pk=restaurantdishreview_id)
        restaurant_review_to_burn.delete()
            
        return redirect(reverse('dineblackapp:checkins'))