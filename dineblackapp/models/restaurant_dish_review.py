from .restaurant import Restaurant
from django.db import models
from django.urls import reverse

class RestaurantDishReview(models.model):

    rating_number = models.CharField(max_length=10)
    dish_name = models.CharField(max_length=25)
    dish_img = models.CharField(max_length=50)
    restaurant_id = models.ForeignKey(Restaurant, related_name=("restaurant"), on_delete=models.DO_NOTHING, null=True, blank=True)
    diner_id = models.ForeignKey(Diner, related_name=("diner"), on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

