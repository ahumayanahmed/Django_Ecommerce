from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')
    preview_des = models.CharField(max_length=255, verbose_name='Short Descriptions')
    description = models.TextField(max_length=1000, verbose_name='Descriptions')
    image = models.ImageField(upload_to='products/')
    slug = models.SlugField(unique=True, blank=True)
    price = models.FloatField()
    old_price = models.FloatField(default=0.00, blank=True, null=True)
    is_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        """Generate unique slug based on product name."""
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the absolute URL of the product using its slug."""
        return reverse('product-detail', kwargs={'slug': self.slug})
    
class ProductImages(models.Model):
     product = models.ForeignKey('Product', on_delete=models.CASCADE)
     image = models.FileField(upload_to='product_gallery')
     created = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return str(self.product.name)
     
     # categoris/models.py
from django.db import models



