from django.urls import path , include
from .views import *


urlpatterns = [
     path('usercreate/', MyUserCreate.as_view() , name='usercreate'),
     path('userlist/', MyUserListView.as_view() , name='userlist'),
]