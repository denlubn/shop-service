from django.contrib import admin

from shop.models import Category, Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("category",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("created_at", "username", "email")

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email


admin.site.register(Category)
