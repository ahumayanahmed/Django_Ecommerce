from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category


# Create your views here.
from django.views.generic import ListView
from categoris.models import Product  # Ensure this matches your actual app name

class Home(ListView):
    model = Product
    template_name = 'categoris/a1.html'
    context_object_name = 'pro'  # This will be used in the template

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "Home/file.html" 
    
class ShopView(TemplateView):
    template_name = "shop/shop.html"  
 


    
    