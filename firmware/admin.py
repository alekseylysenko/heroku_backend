from django.contrib import admin
from .models import Category,Firmware,Technology
# Register your models here.


@admin.register(Firmware)
class FirmwareAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology')


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('title',)

