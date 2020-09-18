import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dineblackapp.models import Restaurant
from ..connection import Connection

def restaurant_list(request):
    if request.method == "GET":
    
        all_restaurants = Restaurant.objects.all()
        
        template_name = 'restaurants/list.html'

        context = {
            'all_restaurants': all_restaurants
        }

        return render(request, template_name, context)