from rest_framework import serializers
from .models import Restaurant


class FullRestaurantSerializer(serializers.ModelSerializer):
    #user = serializers.StringRelatedField()
    class Meta:
        model = Restaurant
        fields = '__all__'


class BasicRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'address']
