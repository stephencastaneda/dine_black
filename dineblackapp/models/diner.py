from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Diner(models.model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=75)
    phone_number = models.CharField(max_length=10)

    class Meta:
        verbose_name = ("diner")
        verbose_name_plural = ("diners")

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse("diner_detail", kwargs={"pk": self.pk})

    

