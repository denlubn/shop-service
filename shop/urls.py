from django.urls import path

from shop.views import ProductListView, order_create_view, order_with_jquery

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/order/", order_create_view, name="order-create"),
    path("products/<int:pk>/order-with-jquery/", order_with_jquery, name="order-with-jquery"),
]
app_name = "shop"
