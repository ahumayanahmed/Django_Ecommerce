from django.http import HttpResponse
from .models import Variation
from django.shortcuts import render
from django.views.generic import ListView, DetailView


# Create your views here.
from django.views.generic import ListView
from categoris.models import Product, ProductImages

class Home(DetailView):
    model = Product
    template_name = 'productdetails/product.html'
    context_object_name = 'prod'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_images"] = ProductImages.objects.filter(product=self.object)
        context["size_variations"] = Variation.objects.sizes().filter(product=self.object)
        context["color_variations"] = Variation.objects.colors().filter(product=self.object)
        return context
