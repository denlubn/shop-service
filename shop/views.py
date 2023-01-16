from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from shop.models import Product, Order, Category
from shop.serializers import (
    CategorySerializer,
    ProductSerializer,
    OrderSerializer,
    ProductListSerializer,
    OrderListSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Pagination(PageNumberPagination):
    page_size = 2
    page_query_param = "page_size"
    max_page_size = 50


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ["category"]
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProductListSerializer

        return ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = Pagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OrderListSerializer

        return OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
