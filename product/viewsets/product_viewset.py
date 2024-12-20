from rest_framework.viewsets import ModelViewSet


from product.Models import Product
from product.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("id")
