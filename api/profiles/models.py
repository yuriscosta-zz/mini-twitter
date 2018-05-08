from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    bio = models.TextField(max_length=280)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=50, unique=True, blank=False)
    # password = models.CharField(max_length=50, blank=False)


# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
