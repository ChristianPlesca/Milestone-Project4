from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def view_cart(request):
    """Render cart.html contents page"""
    return render(request, "cart.html")



def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        request.session['cart'] = cart
        messages.success(request, 'You already have the product in the cart please proceed to checkout to purchase it !!!')    
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('cart'))

def delete_from_cart(request, id):
    """Remove the selected item from the cart"""
    cart = request.session.get('cart', {})
    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('cart'))