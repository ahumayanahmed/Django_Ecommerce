
from django.contrib import admin
from django.urls import path
from . import views
from .views import Cartview


app_name = 'about'
urlpatterns = [
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_to_cart/<int:item_id>/', views.remove_item_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart'), 
    
]