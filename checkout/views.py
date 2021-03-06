from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe
from django.core.mail import send_mail
import time 

stripe.api_key = settings.STRIPE_SECRET

@login_required
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            if request.user.is_authenticated:
                order.user = request.user
                order.email = request.user.email
            else:
                email = request.POST.get('order-email')
                order.email = email
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.success(request, "You have successfully paid")
                request.session['cart'] = {}
                product.sold = True
                product.date_created = timezone.now()
                product.save()
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment")

        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
    

def checkout_bid(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            if request.user.is_authenticated:
                order.user = request.user
                order.email = request.user.email
            else:
                email = request.POST.get('order-email')
                order.email = email
            order.save()

            cart_bid = request.session.get('cart_bid', {})
            bid_total = 0
            for id, quantity in cart_bid.items():
                product = get_object_or_404(Product, pk=id)
                bid_total += quantity * product.bid_price
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount = int(bid_total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.success(request, "You have successfully paid")
                request.session['cart_bid'] = {}
                product.sold = True
                product.date_created = timezone.now()
                product.save()
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment")

        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout_bid.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
    