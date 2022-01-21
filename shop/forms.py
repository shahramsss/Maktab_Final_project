from django import forms
from django.forms import models
from .models import Product, Shop

class ProductRegisterForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'title'}), max_length=56)
    # description = forms.InlineForeignKeyField(widget=forms.InlineForeignKeyField( forms.TextInput(attrs={'class':'w3-input w3-border'}),))
    class Meta:
        model = Product
        fields = ['title', 'categoy','price','description','stock', 'primary_image','image_1','image_2','image_3']
        # fields = '__all__'
        # widgets = {
        #     'price': forms.NumberInput(attrs={'class':'w3-input w3-border'}),
        #     'stock': forms.NumberInput(attrs={'class':'w3-input w3-border'}),
        #     'primary_image': forms.FileInput(attrs={'class':'w3-input w3-border'}),
        #     'image_1': forms.FileInput(attrs={'class':'w3-input w3-border'}),
        #     'image_2': forms.FileInput(attrs={'class':'w3-input w3-border'}),
        #     'image_3': forms.FileInput(attrs={'class':'w3-input w3-border'}),
        # }
    

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
