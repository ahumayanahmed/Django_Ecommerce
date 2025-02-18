
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path
from .views import HomeView
from .views import ShopView


app_name = 'categoris'

urlpatterns = [
path('', HomeView.as_view(), name='home'),
path('shop/', ShopView.as_view(), name='shop'),
path('eloctronic/',views.Home.as_view(), name='Eloctronic'),

]


