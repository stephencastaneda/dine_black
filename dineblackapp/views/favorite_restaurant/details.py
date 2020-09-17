import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dineblackapp.models import FavoriteRestaurant
from ..connection import Connection
 
def favorite_delete(request):
 if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):

            checkin_to_delete = RestaurantDishReview.objects.get(pk=restaurantdishreview_id)
            checkin_to_delete.delete()

        return redirect(reverse('dineblackapp:favorites'))