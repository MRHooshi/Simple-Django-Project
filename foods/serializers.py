from rest_framework import serializers
from .models import Food
from restaurants.serializers import FullRestaurantSerializer


class FullFoodSerializer(serializers.ModelSerializer):
    restaurant = FullRestaurantSerializer(read_only = True)

    class Meta:
        model = Food
        fields = '__all__'


class BasicFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'price', 'is_available']
