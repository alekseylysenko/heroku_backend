from .models import Firmware, Category, Technology, Post, CategoryPost
from rest_framework import viewsets, permissions
from .serializers import FirmwareSerializer, CategorySerializer, TechnologySerializer, PostSerializer, \
    CategoryPostSerializer
from rest_framework.authentication import BasicAuthentication


class FirmwareViewSet(viewsets.ModelViewSet):
    queryset = Firmware.objects.all()
    ordering = ['id']
    ordering_fields = ['id', 'title']
    authentication_classes = (BasicAuthentication,)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = FirmwareSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    ordering = ['id']
    ordering_fields = ['id', 'title']
    authentication_classes = (BasicAuthentication,)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = CategorySerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all().order_by('id')
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = TechnologySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = PostSerializer


class CategoryPostViewSet(viewsets.ModelViewSet):
    queryset = CategoryPost.objects.all().order_by('id')
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = CategoryPostSerializer
