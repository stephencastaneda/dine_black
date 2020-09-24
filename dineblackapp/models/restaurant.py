from django.db import models
from django.urls import reverse

class Restaurant(models.Model):

    name = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    latitude = models.DecimalField(max_digits=10, decimal_places=1)
    longitude = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.CharField(max_length=300, null=True)
    google_maps_link = models.CharField(max_length=300, null=True)
    
    
    class Meta:
        verbose_name = ("restaurant")
        verbose_name_plural = ("restaurants")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Restaurant_detail", kwargs={"pk": self.pk})
    
        
            