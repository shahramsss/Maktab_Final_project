from django.contrib import admin

from .models import Post , Category ,Comment , Image ,Tag
# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =('id','title' , 'short_description' , 'writer', 'created_at')
    prepopulated_fields = {'slug':('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =('id','text')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =('id','title' )
    
