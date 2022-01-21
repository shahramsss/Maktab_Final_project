from django.db import models
from django.db.models.deletion import CASCADE
from account.models import User


class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=56, unique=True)
    type = models.CharField(max_length=56)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=56)
    parent_category = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

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
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    primary_image = models.ImageField(
        upload_to="images", null=True, blank=True)
    image_1 = models.ImageField(upload_to="images", null=True, blank=True)
    image_2 = models.ImageField(upload_to="images", null=True, blank=True)
    image_3 = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(
        decimal_places=2,
        max_digits=15,
    )
    STATUS = (
        ("PAYED", "PAYED"),
        ("NOT_PAYED", "NOT_PAYED"),
    )
    status = models.CharField(
        max_length=9, choices=STATUS, default="NOT_PAYED")

    def __str__(self) -> str:
        return f"order price : {self.total_price}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.product} {self.qty}"
