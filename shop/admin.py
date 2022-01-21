from django import shortcuts
from django.contrib import admin
from .models import Shop , Product , Category

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
