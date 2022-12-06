from rest_framework import serializers

from mounts.models import User, Area, MountainPass


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    model = Area
    fields = '__all__'


class MountainPassSerializer(serializers.ModelSerializer):
    model = MountainPass
    fields = '__all__'
