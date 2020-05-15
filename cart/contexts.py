from django.shortcuts import get_object_or_404
from products.models import Product



def cart_contents(request):
    """Ensure that the contents are available when rendering every page"""

    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}


def cart_contents_bid(request):
    """Ensure that the contents are available when rendering every page"""

    cart_bid = request.session.get('cart_bid', {})
    bid_cart_items = []
    bid_total = 0
    bid_product_count = 0
    for id, quantity in cart_bid.items():
        product = get_object_or_404(Product, pk=id)
        bid_total += quantity * product.bid_price
        bid_product_count += quantity
        bid_cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    return {'bid_cart_items': bid_cart_items, 'bid_total': bid_total, 'bid_product_count':bid_product_count}
    
