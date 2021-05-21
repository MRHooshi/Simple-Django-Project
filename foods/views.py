from rest_framework import viewsets
from .models import Food
from .permissions import IsRestaurantOrIsAdmin
from .serializers import FullFoodSerializer, BasicFoodSerializer
from restaurants.models import Restaurant


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    permission_classes = [IsRestaurantOrIsAdmin, ]

    def get_queryset(self):
        # user is admin
        if self.request.user.is_staff:
            return Food.objects.all()
        # user is restaurant
        return Food.objects.filter(restaurant=self.request.user.restaurant)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullFoodSerializer
        return BasicFoodSerializer

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            restaurant_id = self.request.data['restaurant']
            restaurant = Restaurant.objects.get(pk = restaurant_id)
            serializer.save(restaurant = restaurant)
        else:
            serializer.save(restaurant=self.request.user.restaurant)
