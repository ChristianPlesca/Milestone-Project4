from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


def cart(request):
    """Render cart.html contents page"""
    return render(request, "cart.html")


@login_required
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""

    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart

    return redirect(reverse('cart'))
