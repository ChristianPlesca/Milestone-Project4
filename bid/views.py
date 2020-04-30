from django.shortcuts import render, redirect,get_object_or_404
from products.models import Product
from .forms import BidForm
from django.contrib import messages
from .models import ProductBid, Bid
from django.contrib.auth.decorators import login_required

@login_required
def bid_view(request,pk):
    bid_price = get_object_or_404(Product, pk=pk).bid_price
    product = get_object_or_404(Product, pk=pk)
    bid_form = BidForm(request.POST)
    if request.method == 'POST':
        if bid_form.is_valid():
            bid_form.save()
            bid = bid_form.cleaned_data['bid']
            if bid > bid_price:
                messages.success(request, "Your Bid was succesfully placed")
            elif bid < bid_price:
                messages.error(request, "The bid must be greater than initial bid price")
        else:
            messages.error(request, "The Bid hasn't been submited please try again")
            return redirect('auction')
    args = {'bid_form':bid_form , 'product':product}
    return render(request, 'auction.html',args)
    

