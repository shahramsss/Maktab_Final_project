from django import forms
from django.forms.forms import Form
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )



class UserRegistrationForm(UserCreationForm):
    
    phone = forms.CharField(widget =forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=56, help_text='phone number')
    email=forms.EmailField(widget =forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=128, help_text='Enter a valid email address')
    password1=forms.CharField(widget =forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2=forms.CharField(widget =forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email','phone', 'password1')
         