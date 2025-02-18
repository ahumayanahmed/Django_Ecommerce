from django.contrib import admin
from categoris.models import Category, Product
from categoris.models import ProductImages

class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
