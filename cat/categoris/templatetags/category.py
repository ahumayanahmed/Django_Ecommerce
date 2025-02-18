from django import template
from categoris.models import Category


register = template.Library()  
@register.filter
def get_categories(user):
    if user.is_authenticated:
        cat= Category.objects.filter(parent=None)
        return cat