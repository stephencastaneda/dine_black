from .restaurant import Restaurant
from .diner import Diner
from django.db import models
from django.urls import reverse

class RestaurantRating(models.model):

    rating_number = models.CharField(max_length=10)
    restaurant_id = models.ForeignKey(Restaurant, related_name=("restaurant"), on_delete=models.DO_NOTHING, null=True, blank=True)
    diner_id = models.ForeignKey(Diner, related_name=("diner"), on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = ("restaurant_rating")
        verbose_name_plural = ("restaurant_ratings")


    def __str__(self):
        return self.rating_number