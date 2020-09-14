from .restaurant import Restaurant
from .diner import Diner
from django.db import models
from django.urls import reverse

class RestaurantDishReview(models.Model):

    dish_rating_number = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    dish_name = models.CharField(max_length=25)
    dish_img = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING, null=True, blank=True)
    diner = models.ForeignKey(Diner, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

