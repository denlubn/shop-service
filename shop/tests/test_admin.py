from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from shop.models import Category, Product, Order


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345"
        )
        self.client.force_login(self.admin_user)

    def test_order_all_info_listed(self):
        category = Category.objects.create(name="new_category")
        product = Product.objects.create(name="test_name", category=category, price=15.22)
        order = Order.objects.create(username="new_user", email="user@mail.com", product=product)

        url = reverse("admin:shop_order_changelist")
        res = self.client.get(url)

        self.assertContains(res, order.username)
        self.assertContains(res, order.email)
        self.assertContains(res, product.name)
        self.assertContains(res, product.price)
        self.assertContains(res, category.name)
