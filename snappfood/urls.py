from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('restaurants/', include('restaurants.urls')),
    path('foods/', include('foods.urls')),
]
