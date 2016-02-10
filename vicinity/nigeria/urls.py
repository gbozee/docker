from rest_framework import routers 
from .views import NigeriaLGAViewSet

router = routers.DefaultRouter()
router.register(r'lgas', NigeriaLGAViewSet)
