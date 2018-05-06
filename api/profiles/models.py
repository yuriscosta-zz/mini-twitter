from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
