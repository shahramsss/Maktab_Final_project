from django.db import models
from django.contrib.auth.models import AbstractBaseUser 
from django.core.validators import RegexValidator


class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    email = models.EmailField(max_length=128, unique=True)
    phone = models.BigIntegerField(unique=True)
    city = models.CharField(max_length=56)
    address = models.CharField(max_length=256)
    image = models.ImageField(null= True , blank =True)
    code = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_celler = models.BooleanField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    # is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return f"{self.first_name}' '{self.last_name }"


