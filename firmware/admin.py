from django.contrib import admin
from .models import Category, Firmware, Technology, Post, CategoryPost


@admin.register(Firmware)
class FirmwareAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'url', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology')


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'categoryPost', 'author')


@admin.register(CategoryPost)
class CategoryPostAdmin(admin.ModelAdmin):
    list_display = ('title',)
