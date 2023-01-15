from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from shop.forms import ProductSearchForm, OrderForm
from shop.models import Product, Order


class ProductListView(generic.ListView):
    model = Product
    queryset = Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)

        category = self.request.GET.get("category", "")

        context["search_form"] = ProductSearchForm(initial={
            "category": category
        })

        return context

    def get_queryset(self):
        category = self.request.GET.get("category", "")

        if category:
            return self.queryset.filter(category__name__icontains=category)

        return self.queryset


def order_create_view(request, pk):
    if request.method == "GET":
        context = {
            "form": OrderForm()
        }
        return render(request, "shop/order_form.html", context=context)

    elif request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            Order.objects.create(**form.cleaned_data, product_id=pk)
            return HttpResponseRedirect(reverse("shop:product-list"))

        context = {
            "form": form
        }

        return render(request, "shop/order_form.html", context=context)


def order_with_jquery(request, pk):
    if request.method == "GET":
        context = {
            "order_id": pk
        }
        return render(request, "shop/order_jquery.html", context=context)

    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")

        if username and email:
            Order.objects.create(
                username=username,
                email=email,
                product_id=pk,
            )
            return HttpResponseRedirect(reverse("shop:product-list"))

        context = {
            "error": "Please, provide username & email!"
        }

        return render(request, "shop/order_jquery.html", context=context)
