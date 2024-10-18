from rest_framework.viewsets import ModelViewSet

from product.Models import Category
from product.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("id")
