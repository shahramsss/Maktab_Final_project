from django.urls import path 
from .views import *


app_name = 'account'
urlpatterns = [
    path('logout/',LogoutView.as_view(), name='logout' ),
    path('login/',LoginView.as_view(), name='login' ),
    # path('register/',signup, name='register' ),

    path('register/',RegisterView.as_view(), name='register' ),
    
]
