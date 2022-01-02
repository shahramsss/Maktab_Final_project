from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views import generic
from .models import MyUser
from .forms import MyUserForm
from django.urls import reverse_lazy


class MyUserListView(generic.ListView):
    model = MyUser
    


class MyUserCreate(generic.CreateView):
    model = MyUser
    success_url = reverse_lazy("userlist")
    form_class = MyUserForm
    # fields = "__all__"
    # fields = [ 'first_name','last_name','password','phone',]
