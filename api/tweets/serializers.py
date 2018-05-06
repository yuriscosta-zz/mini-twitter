from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id', 'user', 'content', 'published_date')

