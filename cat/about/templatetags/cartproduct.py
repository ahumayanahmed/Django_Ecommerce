from django import template
from about.models import Cart, Order


# In your cartproduct.py (custom template tags)

from django import template
from about.models import Cart

register = template.Library()

@register.filter
def cart_view(user):
    # Make sure this returns a queryset or an iterable
    try:
        return Cart.objects.filter(user=user, purchased=False)
    except Exception as e:
        # Handle exceptions and log the error if needed
        print(f"Error in cart_view filter: {e}")
        return []

@register.filter
def cart_count(user):
    # Count the number of cart items for the user
    try:
        return Cart.objects.filter(user=user, purchased=False).count()
    except Exception as e:
        # Handle exceptions and log the error if needed
        print(f"Error in cart_count filter: {e}")
        return 0

    
@register.filter
def cart_total(user):
    if user.is_authenticated:
        cart_items = Cart.objects.filter(user=user, purchased=False)
        return sum(float(item.item.price) * item.quantity for item in cart_items)
    return 0.00

