from django.shortcuts import render, redirect,get_object_or_404
from products.models import Product
from .forms import BidForm
from django.contrib import messages
from .models import ProductBid, Bid
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from antique_shop.settings import EMAIL_HOST_USER

@login_required
def bid_view(request,pk):
    product = get_object_or_404(Product, pk=pk)
    bids = get_object_or_404(ProductBid, pk=pk)
    bid_form = BidForm(request.POST, instance=request.user)
    if request.method == 'POST':
        current_bid = request.POST.get("current_bid")
        current_bid = float(current_bid)
        if bid_form.is_valid():
            submit_bid = bid_form.cleaned_data['bid']
            product.bid_price = submit_bid
            product.save()
            if current_bid >= submit_bid:
                messages.error(request, "The Bid must be higher that the current bid price !")
                bid_form = BidForm()
            elif current_bid <= submit_bid:
                messages.success(request, "The bid has been succesfully submited !!!")
                new_bid = Bid(product=bids, bid=submit_bid, user=request.user)
                new_bid.save()
                bid_form = BidForm()
        else:
            messages.error(request,"There has been a problem submiting you bid please try again!")
    else:
        bid_form = BidForm()
    args = {'bid_form':bid_form , 'product':product,'bids':bids}
    return render(request, 'auction.html',args)