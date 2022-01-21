from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.html import format_html
from .forms import UserCreationForm


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'phone','address', 'is_active' , 'is_seller','image')}),
        )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password', 'first_name', 'last_name', 'address','image', 'is_staff', 'is_active', 'phone', 'is_seller')}
    #         ),
    #     )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'address','image', 'is_staff', 'is_active', 'phone', 'is_seller')}
        ),
    )

    filter_horizontal = ()
    list_display = ['email', 'first_name', 'last_name', 'phone','address','show_image', 'is_active','is_seller']

    @admin.display(empty_value='-',description="show image")
    def show_image(self, obj):
        if (obj.image):
            return format_html( '<img src="{}" width=50 height=50/>', obj.image.url, )
        return '-'

admin.site.register(User, CustomUserAdmin)

