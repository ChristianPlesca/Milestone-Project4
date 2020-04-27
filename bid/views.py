from django.shortcuts import render, redirect
from products.models import Product
from .forms import BidForm
from django.contrib import messages

def bid_view(request):
    bid_price = Product.bid_price
    bid_form = BidForm
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
            return redirect('index')
    return render(request, 'index.html',{'bid_form':bid_form})
    

