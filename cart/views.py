from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

""" Render the Cart """
def view_cart(request):
    """Render cart.html contents page"""
    return render(request, "cart.html")

""" Render the Cart for Bid """
def view_cart_bid(request):
    return render(request, 'cart_bid.html')

"""Add a quantity of the specified product to the cart"""
@login_required
def add_to_cart(request, id):
    quantity = 1

    cart = request.session.get('cart', {})
    if id in cart:
        request.session['cart'] = cart
        messages.success(request, 'You already have the product in the cart please proceed to checkout to purchase it !!!')    
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('cart'))

"""Add a quantity of the specified product bid to the cart"""
@login_required
def add_to_cart_bid(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = 1

    cart_bid = request.session.get('cart_bid', {})
    if id in cart_bid:
        request.session['cart_bid'] = cart_bid
        messages.success(request, 'You already have the product in the cart please proceed to checkout to purchase it !!!')    
    else:
        cart_bid[id] = cart_bid.get(id, quantity)

    request.session['cart_bid'] = cart_bid
    return redirect(reverse('view_cart_bid'))

def delete_from_cart(request, id):
    """Remove the selected item from the cart"""
    cart = request.session.get('cart', {})
    cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def delete_from_cart_bid(request, id):
    """Remove the selected item from the cart"""
    cart_bid = request.session.get('cart_bid', {})
    cart_bid.pop(id)

    request.session['cart_bid'] = cart_bid
    return redirect(reverse('view_cart_bid'))