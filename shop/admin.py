from django.contrib import admin

from shop.models import Category, Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("category",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "product_name", "product_category", "product_price")

    def product_name(self, obj):
        return obj.product.name

    def product_category(self, obj):
        return obj.product.category

    def product_price(self, obj):
        return obj.product.price


admin.site.register(Category)
