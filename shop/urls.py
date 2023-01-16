from rest_framework import routers
from django.urls import path, include

from shop.views import CategoryViewSet, ProductViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "shop"
