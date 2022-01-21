from ast import Delete
from itertools import product
from pyexpat import model
from django.db import models
from django.shortcuts import render
from django.views.generic import View, CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from .models import *
from django.urls import reverse_lazy, reverse
from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404



def home(request):
    shops = Shop.objects.filter(user=request.user.id)
    return render(request, "shop/home.html", {'shops': shops})


class PanelView(View):
    def get(self, request):
        try:
            shops = Shop.objects.get(user=request.user.id , is_active=True)
            products = Product.objects.filter(shop=shops)
            return render(request, "shop/panel.html", {'shops': shops, "products": products})
        except Shop.DoesNotExist:
            messages.warning(request, "you have not active shop",)
            return render(request, "shop/panel.html",)

class ShopRegister(CreateView):
    model = Shop
    form_class = ShopRegisterForm
    template_name = "shop/shop_register.html"
    success_url = reverse_lazy("shop:panel")

class ProductRegister(CreateView):
    model = Product
    form_class = ProductRegisterForm
    template_name = "shop/product_register.html"
    success_url = reverse_lazy("shop:panel")

    def form_valid(self, form):
        form.instance.shop =  Shop.objects.get(user=self.request.user , is_active=True)
        form.save()
        return super(ProductRegister, self).form_valid(form)

class ShopRegister(View):
    def get(self, request):
        if not request.user.is_authenticated:
            messages.warning(request, "you must be login!",)
            return redirect(reverse("shop:home"))
        form = ShopRegisterForm()
        return render(request, "shop/shop_register.html", {"form": form})

    def post(self, request):
        obj = Shop.objects.filter(is_active=False, user=request.user).count()
        if obj > 0:
            messages.warning(
                request, "you have an unaccepted shop.  this shop must be activated then you can create new shop",)
            return redirect(reverse("shop:panel"))
        obj = Shop.objects.filter(is_active=True, user=request.user).count()
        if obj > 0:
            messages.warning(
                request, "You can not register more than one shop",)
            return redirect(reverse("shop:panel"))
        form = ShopRegisterForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "your shop is created",)
            return redirect(reverse("shop:panel"))


class DeleteShop(UpdateView):
    form_class = DeleteShopForm
    model = Shop
    template_name = 'shop/shop_delete.html'
    success_url = reverse_lazy('shop:home')
