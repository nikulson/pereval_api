from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
import json
from mounts.models import User, Area, MountainPass
from mounts.serializers import UserSerializer, AreaSerializer, MountainPassSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class MountainPassViewSet(viewsets.ModelViewSet):
    queryset = MountainPass.objects.all()
    serializer_class = MountainPassSerializer


def submitData(request):
    if request.method == 'POST':
        json_params = json.loads(request.body)

        mountain_pass = MountainPass.objects.create(
            title=json_params['title'],
            alt_title=json_params['alt_title'],
            longitude=json_params['longitude'],
            latitude=json_params['latitude'],
            height=json_params['height'],
            user=User.objects.create(
                first_name=json_params['first_name'],
                last_name=json_params['last_name'],
                email=json_params['email'],
            )

        )
        return HttpResponse(json.dumps({
            "title": mountain_pass.title,
            "alt_title": mountain_pass.alt_title,
            "longitude": mountain_pass.longitude,
            "latitude": mountain_pass.latitude,
            "height": mountain_pass.height,
            "user": mountain_pass.user,
        }))


