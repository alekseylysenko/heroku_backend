from rest_framework import serializers
from .models import Category, Technology, Firmware, Post, CategoryPost


class FirmwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firmware
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPost
        fields = '__all__'