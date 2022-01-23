from django.urls import path 
from .views import *


app_name = 'shop'
urlpatterns = [
    path('home/',home, name='home' ),
    path('shopregister/',ShopRegister.as_view(), name='shopregister' ),
    path('panel/',PanelView.as_view(), name='panel' ),
    path('shopdelete/<int:pk>',ShopDelete.as_view(), name='shopdelete' ),
    path('productregister/',ProductRegister.as_view(), name='productregister' ),
    path('shopupdate/<int:pk>',ShopUpdate.as_view(), name='shopupdate' ),
    path('productupdate/<int:pk>',ProductUpdate.as_view(), name='productupdate' ),
    path('productdelete/<int:pk>',ProductDelete.as_view(), name='productdelete' ),
    path('productstate/<int:pk>',ProductState.as_view(), name='productstate' ),
    path('orderlist',OrderView.as_view(), name='orderlist' ),


    
]
