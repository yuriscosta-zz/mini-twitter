from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    bio = models.TextField(max_length=280)
