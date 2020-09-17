import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dineblackapp.models import Restaurant, RestaurantDishReview
from django.forms import ModelForm
from ..connection import Connection


def get_restaurants():

        all_restaurants = Restaurant.objects.all()

        return(all_restaurants)

def get_restaurant_dish_review(restaurantdishreview_id):

    single_restaurant_review = RestaurantDishReview.objects.get(pk=restaurantdishreview_id)

    return(single_restaurant_review)

def checkin_form(request):
    if request.method == 'GET':
        restaurants = get_restaurants()
        template = 'checkins/list.html'
        context = {
            'all_restaurants': restaurants
        }

        return render(request, template, context)

def checkin_edit_form(request, restaurantdishreview_id):
    if request.method == 'GET':
        dish_review = get_restaurant_dish_review(restaurantdishreview_id)
        restaurants = get_restaurants()

        template = 'checkins/edit_form.html'
        context = {
            'dish_review': dish_review,
            'all_restaurants': restaurants
        }

        return render(request, template, context)