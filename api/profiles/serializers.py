from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'password', 'bio')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile = Profile(**validated_data)
        profile.set_password(validated_data['password'])
        profile.save()

        return profile

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.bio = validated_data['bio']
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()

        return instance
