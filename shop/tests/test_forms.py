from django.test import TestCase

from shop.forms import OrderForm


class FormsTests(TestCase):
    def test_order_creation_form(self):
        form_data = {
            "username": "new_user",
            "email": "user@mail.com"
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
