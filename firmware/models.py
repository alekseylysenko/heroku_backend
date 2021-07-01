from django.db import models
from django.contrib.auth.models import User


class Firmware(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Technology(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    body = models.TextField()
    categoryPost = models.ForeignKey('CategoryPost', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CategoryPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')

    class Meta:
        verbose_name = "Категории для Статьи"
        verbose_name_plural = "Категории для Статей"

    def __str__(self):
        return self.title


