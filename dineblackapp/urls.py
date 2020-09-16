from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import *

app_name = "dineblackapp"

urlpatterns = [
  path('restaurants/', restaurant_list, name='restaurants'),
  path('logout/', logout_user, name='logout'),
  path('register/', register_user, name="register"),
  path('', restaurant_list, name='home'),
  path('checkins', check_in_list, name='checkins')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)