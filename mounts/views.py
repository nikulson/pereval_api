from django.shortcuts import render
from rest_framework import generics

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
