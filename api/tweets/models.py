from django.db import models
from profiles.models import Profile


class Tweet(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-published_date',)
