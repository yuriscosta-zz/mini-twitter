from .models import Profile
from .serializers import ProfileSerializer

from rest_framework import permissions, viewsets, status
from rest_framework.response import Response


class ProfileViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = Profile.objects.filter(
            pk=kwargs.get('pk')
        ).first()
        serializer = ProfileSerializer(instance)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = Profile.objects.filter(
            pk=kwargs.get('pk')
        ).first()

        if (instance != request.user):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = ProfileSerializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = Profile.objects.filter(
            pk=kwargs.get('pk'),
        ).first()

        if (instance != request.user):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)
