from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import *

app_name = "dineblackapp"

urlpatterns = [
  path('restaurants/', restaurant_list, name='restaurants'),
  path('logout/', logout_user, name='logout'),
  path('register/', register_user, name="register"),
  path('', restaurant_list, name='home'),
  path('checkins', check_in_list, name='checkins'),
  path('favorites', favorite_list, name='favorites'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('favorites/<int:favoriterestaurant_id>/', favorite_delete, name='favorite'),
  path('checkins/<int:restaurantdishreview_id>/', checkin_change, name='checkin'),
  path('checkins/<int:restaurantdishreview_id>/form/', checkin_edit_form, name='checkin_edit_form'),
  path('restaurants/<int:restaurant_id>/', restaurant_details, name='restaurant'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)