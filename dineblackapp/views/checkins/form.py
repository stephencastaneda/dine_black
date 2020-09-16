import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dineblackapp.models import Restaurant
from django.forms import ModelForm
from ..connection import Connection


def get_restaurants():

        all_restaurants = Restaurant.objects.all()

        return(all_restaurants)

def checkin_form(request):
    if request.method == 'GET':
        restaurants = get_restaurants()
        template = 'checkins/list.html'
        context = {
            'all_restaurants': restaurants
        }

        return render(request, template, context)
