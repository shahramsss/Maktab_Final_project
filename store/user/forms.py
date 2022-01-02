from django import forms
from django import forms
from django.forms import fields, models
from .models import MyUser

class MyUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        # fields= '__all__'
        fields = [ 'first_name','last_name','phone',]
    
    def clean_password2(self):
        pwd1 = self.cleaned_data.get('password1')
        pwd2 = self.cleaned_data.get('password2')
        if not pwd1 or not pwd2:
            raise forms.ValidationError('Password is empty')
        if pwd1 != pwd2:
            raise forms.ValidationError('Passwords do not match')
        return pwd2

    def save(self, commit=True):
        customuser = super().save(commit=False)
        customuser.set_password(self.cleaned_data['password1'])
        if commit:
            customuser.save()
        return customuser