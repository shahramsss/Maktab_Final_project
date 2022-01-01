import django
from django.urls import path , include
from .views import *


urlpatterns = [
    path('posts/', posts , name='posts'),
    path('detail/<int:post_id>', post_detail_by_id , name='detail'),
    path('detail/<str:post_slug>', post_detail_by_slug , name='detail'),
    path('categorys/', categorys , name='categorys'),
    path('category_details/<str:category_title>', category_details , name='category_details'),
    path('allposts/', PostListView.as_view() , name='allposts'),
    path('getpost/<slug:post_slug>', GetPost.as_view() , name='allposts'),
    # path('newslug/<slug:new_slug>', check_slug , name='check_slug'),
    path('adduser/', add_user , name='check_slug'),
    path('',include('django.contrib.auth.urls')),
    path('regitser/', register , name='register'),
    path('tags/', Tags.as_view() , name='tags'),
    path('filter-post/<str:category>',filter_posts , name='filter_posts'),
    path('editcategory/<int:category_id>',edit_category , name='edit_category'),
    path('addcategory/',add_category , name='add_category'),
    path('deletecategory/<int:category_id>',delete_category , name='delete_category'),
    path('newpost/',new_post , name='new_post'),
    path('tagpost/<str:tag>',tag_filter_post , name='tag_filter_post'),
    path('addtag/',add_tag , name='add_tag'),
    path('deletetag/<int:tag_id>',delete_tag , name='delete_tag'),
    path('edittag/<int:tag_id>',edit_tag , name='edit_tag'),
    path('search/',search , name='search'),
    path('register2/', register2 ,name='register2'),
    path('login2/', login_view ,name='login_view'),

    
] 
