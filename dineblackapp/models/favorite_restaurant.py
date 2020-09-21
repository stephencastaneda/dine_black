from .restaurant import Restaurant
from .diner import Diner
from django.db import models
from django import forms

class FavoriteRestaurant(models.Model):

    restaurant = models.ForeignKey(Restaurant, related_name=("restaurant"), on_delete=models.DO_NOTHING, null=True, blank=True)
    diner = models.ForeignKey(Diner, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = ("favorite_restaurant")
        verbose_name_plural = ("favorite_restaurants")


    def __str__(self):
        return self.restaurant_id
    
    # def clean_restaurant_name(self):
    #     restaurant_name = self.cleaned_data.get('restaurant')

    #     for instance in Restaurant.objects.all():
    #         if instance.restaurant == restaurant_name:
    #             raise forms.ValidationError('you already added this restaurant')
    #     return restaurant_name
   