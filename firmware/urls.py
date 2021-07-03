from rest_framework import routers
from .api import FirmwareViewSet, CategoryViewSet, TechnologyViewSet, PostViewSet, CategoryPostViewSet, ChatViewSet

routers = routers.DefaultRouter()
routers.register('api/firmware', FirmwareViewSet, 'firmware'),
routers.register('api/category', CategoryViewSet, 'category'),
routers.register('api/technology', TechnologyViewSet, 'technology')
routers.register('api/posts', PostViewSet, 'posts')
routers.register('api/category_post', CategoryPostViewSet, 'category_post')
routers.register('api/chat', ChatViewSet, 'chat')
urlpatterns = routers.urls

