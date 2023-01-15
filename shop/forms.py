from django import forms

from shop.models import Order


class ProductSearchForm(forms.Form):
    category = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by category"})
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("username", "email")
