from django.db import models
from django.db.models.deletion import CASCADE
from user.models import MyUser


class Shop (models.Model):
    title = models.CharField(max_length=56)
    type = models.CharField(max_length=56)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=56)
    parent_category = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True,)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=56)
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)
    categoy = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.DecimalField(decimal_places=2, max_digits=15,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    primary_image = models.ImageField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Order (models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=15,)
    STATUS = (('PAYED', 'PAYED'), ('NOT_PAYED', 'NOT_PAYED'),)
    status = models.CharField(max_length=9, choices=STATUS, default="NOT_PAYED")

    def __str__(self) -> str:
        return f"order price : {self.total_price}"


class OrderItem (models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.product} {self.qty}"
