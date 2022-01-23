from django import forms
from django.forms import models
from .models import Product, Shop

class ProductRegisterForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'title'}), max_length=56)
    # description = forms.InlineForeignKeyField(widget=forms.InlineForeignKeyField( forms.TextInput(attrs={'class':'w3-input w3-border'}),))
    class Meta:
        model = Product
        fields = ['title', 'categoy','price','description','stock', 'primary_image','image_1','image_2','image_3']
    

class ShopRegisterForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'title'}), max_length=56)
    type = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'type'}), max_length=56)

    class Meta:
        model = Shop
        fields = ('title', 'type')


class DeleteShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ()

    def save(self, commit=True):
        isactive = super().save(commit=False)
        isactive.is_active = False
        if commit:
            isactive.save()
            return isactive

class ProductStateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_active']

    # def save(self, commit=True):
    #     isactive = super().save(commit=False)
    #     if isactive.is_active == True:
    #         isactive.is_active = False
    #     else:
    #         isactive.is_active = True
    #     if commit:
    #         isactive.save()
    #         return isactive