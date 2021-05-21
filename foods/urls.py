from rest_framework import routers
from .views import FoodViewSet

router = routers.SimpleRouter()
router.register('', FoodViewSet)
urlpatterns = router.urls