from django.db import models


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
    title = models.CharField(max_length=100)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


