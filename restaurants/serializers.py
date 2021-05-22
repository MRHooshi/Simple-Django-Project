from rest_framework import serializers
from .models import Restaurant
from foods.models import Food


class ListFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'price']


class FullRestaurantSerializer(serializers.ModelSerializer):
    foods = ListFoodSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'


class BasicRestaurantSerializer(serializers.ModelSerializer):
    foods = ListFoodSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['name', 'address']
