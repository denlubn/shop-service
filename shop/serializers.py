from rest_framework import serializers

from shop.models import Category, Product, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "category", "price")


class ProductListSerializer(ProductSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field="name")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "products")


class OrderListSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Order
        fields = ("id", "created_at", "username", "email", "products")
