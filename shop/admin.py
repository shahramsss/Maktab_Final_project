from django import shortcuts
from django.contrib import admin
from .models import *

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "total_price")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ( "product", "qty", "price")
    exclude = ['price']