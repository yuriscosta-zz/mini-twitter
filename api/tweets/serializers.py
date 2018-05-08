from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id', 'content', 'published_date')
        read_only_fields = ('published_date',)

    def create(self, validated_data):
        tweet = Tweet(**validated_data)
        tweet.user = self.context['request'].user
        tweet.save()

        return tweet
