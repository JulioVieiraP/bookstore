from django.db import models

from product.Models.category import Category

class Product(models.Model):
    Title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveSmallIntegerField(null=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)