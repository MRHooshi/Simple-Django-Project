from rest_framework import viewsets
from .models import Restaurant
from .serializers import FullRestaurantSerializer, BasicRestaurantSerializer
from .permissions import IsAdminOrReadOnly


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullRestaurantSerializer
        return BasicRestaurantSerializer
