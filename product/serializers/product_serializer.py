from rest_framework import serializers

from product.Models.product import Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.Serializer):
    Category = CategorySerializer(required=True, many=True)

    class Meta:
        model = Product
        fields = ('Title', 'description', 'price', 'active', 'category')