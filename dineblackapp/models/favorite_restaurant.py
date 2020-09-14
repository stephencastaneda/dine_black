from .restaurant import Restaurant
from .diner import Diner

class FavoriteRestaurant(models.model):

    restaurant_id = models.ForeignKey(Restaurant, related_name=("restaurant"), on_delete=models.DO_NOTHING, null=True, blank=True)
    diner_id = models.ForeignKey(Diner, related_name=("diner"), on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = ("favorite_restaurant")
        verbose_name_plural = ("favorite_restaurants")


    def __str__(self):
        return self.restaurant_id