from django.contrib import admin

from .models import *

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Shop)
# admin.site.register(Order)
admin.site.register(OrderItem)




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('title',)
    # date_hierarchy =('',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active',)
    list_filter = ('title', 'price',)
    search_fields = ('title', 'price')
    ordering = ('title', 'price',)
    date_hierarchy = 'updated_at'


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)
    ordering = ('title',)
    # date_hierarchy =('',)

    @admin.action(description='Mark selected shops to active ')
    def make_published(ShopAdmin, request, queryset):
        queryset.update(is_active=True)

    actions = [make_published]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','total_price','status',)
    list_filter = ('status',)
    search_fields = ('total_price',)
    ordering = ('total_price',)
    date_hierarchy ='updated_at'


