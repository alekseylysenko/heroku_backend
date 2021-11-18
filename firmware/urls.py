from django.urls import path
from rest_framework import routers

from . import api
from .api import FirmwareViewSet, CategoryViewSet, TechnologyViewSet, PostViewSet, CategoryPostViewSet

routers = routers.DefaultRouter()
routers.register('api/firmware', FirmwareViewSet, 'firmware'),
routers.register('api/category', CategoryViewSet, 'category'),
routers.register('api/technology', TechnologyViewSet, 'technology')
routers.register('api/posts', PostViewSet, 'posts')
routers.register('api/category_post', CategoryPostViewSet, 'category_post')

urlpatterns = routers.urls

