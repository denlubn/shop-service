from django.test import TestCase, Client
from django.urls import reverse

from shop.models import Product, Category, Order

PRODUCT_URL = reverse("shop:product-list")


class ProductTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_retrieve_products(self):
        category = Category.objects.create(name="test_category")
        product1 = Product.objects.create(name="product1", category=category, price=15.22)
        product2 = Product.objects.create(name="product2", category=category, price=15.25)

        response = self.client.get(PRODUCT_URL)
        products = Product.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["product_list"]), list(products))
        self.assertTemplateUsed(response, "shop/product_list.html")


class OrderTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_order_product(self):
        category = Category.objects.create(name="test_category")
        product = Product.objects.create(name="test_name", category=category, price=15.22)

        form_data = {
            "username": "new_user",
            "email": "user@mail.com"
        }
        get_response = self.client.get(reverse("shop:order-create", kwargs={"pk": product.id}))
        post_response = self.client.post(reverse("shop:order-create", kwargs={"pk": product.id}), data=form_data)
        new_order = Order.objects.get(username=form_data["username"])

        self.assertEqual(new_order.email, form_data["email"])
        self.assertEqual(new_order.product, product)
        self.assertTemplateUsed(get_response, "shop/order_form.html")
        self.assertRedirects(post_response, PRODUCT_URL)

    def test_order_with_jQuery(self):
        category = Category.objects.create(name="test_category")
        product = Product.objects.create(name="test_name", category=category, price=15.22)

        form_data = {
            "username": "new_user",
            "email": "user@mail.com"
        }
        get_response = self.client.get(reverse("shop:order-with-jquery", kwargs={"pk": product.id}))
        post_response = self.client.post(reverse("shop:order-with-jquery", kwargs={"pk": product.id}), data=form_data)
        new_order = Order.objects.get(username=form_data["username"])

        self.assertEqual(new_order.email, form_data["email"])
        self.assertEqual(new_order.product, product)
        self.assertTemplateUsed(get_response, "shop/order_jquery.html")
        self.assertRedirects(post_response, PRODUCT_URL)
