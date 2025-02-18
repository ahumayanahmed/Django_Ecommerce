
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('product/<slug:slug>/', views.Home.as_view(), name='product-detail'),
]




