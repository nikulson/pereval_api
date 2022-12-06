from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from mounts.models import User, Area, MountainPass
from mounts.serializers import UserSerializer, AreaSerializer, MountainPassSerializer


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AreaAPIView(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class MountainPassAPIView(generics.ListAPIView):
    queryset = MountainPass.objects.all()
    serializer_class = MountainPassSerializer

    def submitData(self, request):
        post_new = MountainPass.objects.create(
            title=request.data['title'],
            author=request.data['author'],
            longitude=request.data['longitude'],
            latitude=request.data['latitude'],
            height=request.data['height'],
            images=request.data['images'],
        )
        return Response({'submitData': model_to_dict(post_new)})

