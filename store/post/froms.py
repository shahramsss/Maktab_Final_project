from django import forms
from django.contrib.auth import login
from django.contrib.auth.models import User 
from django.forms import fields, models
from django.contrib.auth.forms import UserCreationForm 
from .models import Category, Comment, Post, Tag
# from blog.post.models import Category

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class NewUserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ("username", "email", "password")

	
	
class FormCategory(forms.ModelForm):
    title = forms.CharField(max_length=255 , min_length=3 , label='دسته بندی :',error_messages={'required':'لطفا دسته بندی را درست وارد کنید !'})
    class Meta:
        model = Category
        fields = '__all__'


class FormDeleteCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields= []


class FormPots(forms.ModelForm):
    class Meta:
        model = Post
        fields= '__all__'
        exclude = ['writer'] 


class FormTag(forms.ModelForm):
    title = forms.CharField(max_length=255 , min_length=3 , label=' تگ :',error_messages={'required':'لطفا تگ را درست وارد کنید !'})

    class Meta:
        model = Tag
        fields= '__all__'


class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title' , 'text']

        labels = {
            'title': 'عنوان',
            'text' : 'نظر'
        }
        error_messages = {
            'title' :{
                
            }
        }



class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']


# class UsersLoginForm(forms.Form):
# 	username = forms.CharField()
# 	password = forms.CharField(widget = forms.PasswordInput,)
    


from django.contrib.auth import authenticate
from django import forms

class UsersLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput,)

	def __init__(self, *args, **kwargs):
		super(UsersLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"username"})
		self.fields['password'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"password"})

	def clean(self, *args, **keyargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username = username, password = password)
			if not user:
				raise forms.ValidationError("نام کاربری یا رمز عبور اشتباه است !")
			if not user.check_password(password):
				raise forms.ValidationError("رمز عبور اشتباه است !")
			if not user.is_active:
				raise forms.ValidationError("User is no longer active")

		return super(UsersLoginForm, self).clean(*args, **keyargs)
 