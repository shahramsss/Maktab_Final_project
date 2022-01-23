from django.db import models
from django.db.models.deletion import CASCADE
from account.models import User


class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING , unique=True)
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

   

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    qty = models.PositiveIntegerField(null=True, blank=True, default=1)
    price =models.DecimalField(max_digits=15, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return str(self.product)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.qty
        return super().save(*args, **kwargs)
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    order = models.ForeignKey(OrderItem, on_delete=models.CASCADE ,related_name="order_of_orderitem")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(decimal_places=2,max_digits=15,)
    STATUS = (("PAYED", "PAYED"),("NOT_PAYED", "NOT_PAYED"),)
    status = models.CharField(max_length=9, choices=STATUS, default="NOT_PAYED")

    def __str__(self) -> str:
        return f"order price : {self.total_price}"