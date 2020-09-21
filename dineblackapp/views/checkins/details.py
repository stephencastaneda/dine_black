from django.urls import reverse
from django.shortcuts import render, redirect
from dineblackapp.models import RestaurantDishReview
from ..connection import Connection

def checkin_change(request, restaurantdishreview_id):
    if request.method == 'GET':

        restaurant_dish_review = RestaurantDishReview.objects.get(pk=restaurantdishreview_id)

        template = 'checkins/list.html'
        context = {
            'restaurant_dish_review': restaurant_dish_review
        }
        
        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST

        if (
          "actual_method" in form_data
          and form_data["actual_method"] == "PUT"
        ):

          checkin_to_update = RestaurantDishReview.objects.get(pk=restaurantdishreview_id)

          checkin_to_update.dish_name = form_data["dish_name"]
          checkin_to_update.dish_image = form_data["dish_image"]
          checkin_to_update.dish_rating_number = form_data["dish_rating_number"]
          checkin_to_update.restaurant_id = form_data["restaurant"]

          checkin_to_update.save()

          return redirect(reverse('dineblackapp:checkins'))

    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):

            checkin_to_delete = RestaurantDishReview.objects.get(pk=restaurantdishreview_id)
            checkin_to_delete.delete()

        return redirect(reverse('dineblackapp:checkins'))