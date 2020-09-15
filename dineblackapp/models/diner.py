from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse

class Diner(models.Model):

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

    @receiver(post_save, sender=User)
    def create_diner(sender, instance, created, **kwargs):
        if created:
            Diner.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_diner(sender, instance, **kwargs):
        instance.diner.save()
    

