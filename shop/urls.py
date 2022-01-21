from django.urls import path 
from .views import *


app_name = 'shop'
urlpatterns = [
    path('home/',home, name='home' ),
    path('shopregister/',ShopRegister.as_view(), name='shopregister' ),
    path('panel/',PanelView.as_view(), name='panel' ),
    path('delete/<int:pk>',DeleteShop.as_view(), name='shopdelete' ),
    path('productregister/',ProductRegister.as_view(), name='productregister' ),

    
]
