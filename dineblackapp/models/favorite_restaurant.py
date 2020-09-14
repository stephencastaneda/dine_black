from .restaurant import Restaurant
from .diner import Diner
from django.db import models

class FavoriteRestaurant(models.Model):

    restaurant = models.ForeignKey(Restaurant, related_name=("restaurant"), on_delete=models.DO_NOTHING, null=True, blank=True)
    diner = models.ForeignKey(Diner, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = ("favorite_restaurant")
        verbose_name_plural = ("favorite_restaurants")


    def __str__(self):
        return self.restaurant_id