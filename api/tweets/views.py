from .models import Tweet
from .serializers import TweetSerializer

from rest_framework import permissions, viewsets, status
from rest_framework.response import Response


class TweetViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Tweet.objects.all().exclude(
            user=request.user
        )[:10]
        serializer = TweetSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = TweetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = Tweet.objects.filter(
            pk=kwargs.get('pk')
        ).first()
        serializer = TweetSerializer(instance)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = Tweet.objects.filter(
            pk=kwargs.get('pk')
        ).first()
        serializer = TweetSerializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = Tweet.objects.filter(
            pk=kwargs.get('pk'),
        )
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)
