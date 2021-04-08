from .models import Firmware, Category, Technology
from rest_framework import viewsets, permissions
from .serializers import FirmwareSerializer, CategorySerializer, TechnologySerializer


class FirmwareViewSet(viewsets.ModelViewSet):
    queryset = Firmware.objects.all()
    ordering = ['id']
    ordering_fields = ['id', 'title']
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FirmwareSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all().order_by('id')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TechnologySerializer


