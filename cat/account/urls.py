
from django.contrib import admin
from django.urls import path
from . import views
from .views import register, success


urlpatterns = [
    path('w/',views.account, name='acc'),
    path("register/", views.register, name="register"),
    path("success/", success, name="success"),
]

    
