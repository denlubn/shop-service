from django.db.models.functions import datetime
from django.test import TestCase

from shop.models import Category, Product, Order


class ModelsTests(TestCase):
    def test_category_str(self):
        category = Category.objects.create(name="test_name")

        self.assertEqual(str(category), "test_name")

    def test_product_str(self):
        category = Category.objects.create(name="test_name")
        product = Product.objects.create(name="test_name", category=category, price=15.22)

        self.assertEqual(str(product), "test_name")

    def test_order_str(self):
        category = Category.objects.create(name="test_name")
        product = Product.objects.create(name="test_name", category=category, price=15.22)
        order = Order.objects.create(username="new_user", email="user@mail.com", product=product)

        self.assertEqual(str(order.created_at), str(order))
