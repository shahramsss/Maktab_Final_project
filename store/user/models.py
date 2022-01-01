from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    email = models.EmailField(max_length=128, unique=True)
    phone = models.BigIntegerField(max_length=56)
    is_active = models.BooleanField(default=True)
    city = models.CharField(max_length=56)
    address = models.CharField(max_length=256)
    image = models.ImageField(null= True , blank =True)
    code = models.PositiveIntegerField()
    is_celler = models.BooleanField()


    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return f"{self.first_name}' '{self.last_name }"


