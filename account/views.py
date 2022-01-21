from .forms import UserLoginForm
from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls.base import reverse
from django.views import generic
from .forms import *
from django.views.generic import View
from account.models import User
from django.urls import reverse_lazy


class RegisterView(View):
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect(reverse("shop:panel"))

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("shop:panel"))
        form = UserRegistrationForm()
        return render(request, "account/register.html", {"form": form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.warning(request,"you are log outed", "warning")
        return redirect("shop:home")

class LoginView(View):
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd["email"], password=cd["password"])
            if user is not None:
                if  not user.is_seller:
                    messages.warning(request, "you must be seller", "warning")
                    return redirect("account:login")

                if user.is_active:
                    login(request, user)
                    messages.success(request, "you logged in successfully", "success")
                    return redirect("shop:panel")
            else:
                messages.warning(request, "username and password is wrong", "warning")
                return redirect("account:login")
        
    def get(self, request):
        form = UserLoginForm()
        return render(request, "account/login.html", {"form": form})
        