from django.contrib import admin
from .models import MyUser

from django.utils.html import format_html
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','phone','show_image')
    list_filter = ('email',)
    search_fields = ('first_name' , 'last_name')
    ordering = ('first_name',)
    

    @admin.display(empty_value='-',description="show image")
    def show_image(self, obj):
        if (obj.image):
            return format_html( '<img src="{}" width=50 height=50/>', obj.image.url, )
        return '-'