from rest_framework import routers
from .api import FirmwareViewSet, CategoryViewSet, TechnologyViewSet


routers = routers.DefaultRouter()
routers.register('api/firmware', FirmwareViewSet, 'firmware'),
routers.register('api/category', CategoryViewSet, 'category'),
routers.register('api/technology', TechnologyViewSet, 'technology')

urlpatterns = routers.urls

