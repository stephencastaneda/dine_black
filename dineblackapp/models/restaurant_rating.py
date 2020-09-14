from .restaurant import Restaurant
from .diner import Diner
from django.db import models
from django.urls import reverse

class RestaurantRating(models.Model):

    restaurant_rating_number = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING, null=True, blank=True)
    diner = models.ForeignKey(Diner, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = ("restaurant_rating")
        verbose_name_plural = ("restaurant_ratings")


    def __str__(self):
        return self.rating_number