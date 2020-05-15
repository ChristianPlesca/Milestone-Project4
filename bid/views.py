from django.shortcuts import render, redirect,get_object_or_404,reverse
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
    current_bid = Bid.objects.filter(product=bids).order_by('-bid').first()
    if request.method == 'POST':
        expiry_date = request.POST.get("expiryDateText")
        print(expiry_date)
        if expiry_date == "BID EXPIRED !!!":
            product.expired = True
            product.save()
        if bid_form.is_valid():
            submit_bid = bid_form.cleaned_data['bid']
            if submit_bid:
                if current_bid.bid >= submit_bid:
                    messages.error(request, "The Bid must be higher that the current bid price !")
                    bid_form = BidForm()
                    return redirect("bid_view", product.id)
                elif current_bid.bid < submit_bid:
                    messages.success(request, "The bid has been succesfully submited !!!")
                    new_bid = Bid(product=bids, bid=submit_bid, user=request.user)
                    new_bid.save()
                    product.bid_price = submit_bid
                    product.save()
                    bid_form = BidForm()
                    return redirect("bid_view",product.id)
        else:
            messages.error(request,"There has been a problem submiting you bid please try again!")
    else:
        bid_form = BidForm()
    args = {'bid_form':bid_form , 'product':product,'bids':bids,'current_bid':current_bid}
    return render(request, 'auction.html',args)