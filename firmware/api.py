from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Firmware, Category, Technology, Post, CategoryPost, Chat
from rest_framework import viewsets, permissions, filters
from .serializers import FirmwareSerializer, CategorySerializer, TechnologySerializer, PostSerializer, \
    CategoryPostSerializer, ChatSerializer
from rest_framework.authentication import BasicAuthentication


class FirmwareViewSet(viewsets.ModelViewSet):
    search_field = ['title']
    filter_backends = (SearchFilter, DjangoFilterBackend)
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
    search_field = ['title', 'body']
    filter_backends = [filters.SearchFilter]
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


class ChatViewSet(viewsets.ModelViewSet):

    queryset = Chat.objects.all().order_by('id')
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = ChatSerializer


