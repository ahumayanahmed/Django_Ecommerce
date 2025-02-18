from django.db import models
from categoris.models import Product

# Custom Manager for filtering variations
class VariationManager(models.Manager):
    def sizes(self):
        return super().filter(variation='size')  # Correct way to filter sizes
    
    def colors(self):
        return super().filter(variation='color')  # Correct way to filter colors

VARIATION_TYPE = (
    ('size', 'Size'),
    ('color', 'Color'),
)

class Variation(models.Model):
    variation = models.CharField(max_length=100, choices=VARIATION_TYPE)  # Fixed typo from "varitation"
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variations")
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()  # Assign custom manager

    def __str__(self):
        return f"{self.name} - {self.variation}"
