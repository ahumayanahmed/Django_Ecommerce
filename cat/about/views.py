from django.shortcuts import get_object_or_404, redirect
from categoris.models import Product
from about.models import Cart, Order
from django.views.generic import TemplateView
from django.shortcuts import render

def add_to_cart(request, item_id):
    # Get the Product instance using the item_id
    product = get_object_or_404(Product, id=item_id)
    
    # Get data from the POST request
    quantity = request.POST.get('quantity')
    try:
        quantity = int(quantity) if quantity else 1
    except (ValueError, TypeError):
        quantity = 1  # Default to 1 if invalid input

    # Use default empty strings if size or color is not provided
    size = request.POST.get('size') or ''
    color = request.POST.get('color') or ''

    # Try to get or create a Cart object based on product, user, size, color, and purchased status
    try:
        order_item, created = Cart.objects.get_or_create(
            item=product,
            user=request.user,
            purchased=False,
            size=size,
            color=color,
        )
    except Cart.MultipleObjectsReturned:
        # If duplicates exist, merge them
        cart_qs = Cart.objects.filter(
            item=product,
            user=request.user,
            purchased=False,
            size=size,
            color=color,
        )
        # Choose the first cart item and merge quantities from duplicates
        order_item = cart_qs.first()
        total_quantity = sum(item.quantity for item in cart_qs)
        order_item.quantity = total_quantity
        order_item.save()
        # Remove any duplicate items, keeping only the merged one
        cart_qs.exclude(pk=order_item.pk).delete()
        created = False

    # Update the quantity: if the item already existed, add to it; otherwise, set it.
    if not created:
        order_item.quantity += quantity
    else:
        order_item.quantity = quantity
    order_item.save()

    # Now handle the Order: add this cart item to the active order, or create one if it doesn't exist.
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs.first()
        # Only add if it's not already in the order
        if not order.orderitems.filter(pk=order_item.pk).exists():
            order.orderitems.add(order_item)
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item)

    return redirect('categoris:home')




class Cartview(TemplateView):
    template_name = "About/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
     
        try:
            cart_items = Cart.objects.filter(user=self.request.user, purchased=False)
        except ValueError as e:
            cart_items = []  
            print(f"Error fetching cart items: {e}")
        
        context['cart_items'] = cart_items
        return context
        
#remove cart product
def remove_item_from_cart(request, item_id):
    item = get_object_or_404(Product, id=item_id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs.first()
        cart_item_qs = Cart.objects.filter(user=request.user, item=item, purchased=False)

        if cart_item_qs.exists():
            cart_item = cart_item_qs.first()
            order.orderitems.remove(cart_item)
            cart_item.delete()

    return redirect('about:cart')


#view cart create
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user, purchased=False)  
    return render(request, 'about/cart.html', {'cart_items': cart_items})




