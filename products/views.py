from django.shortcuts import render,get_object_or_404
from .models import Product, ProductsPictures
from bid.models import UserBid,Bid

def home_page(request):
    """Display index page"""
    products = Product.objects.all().order_by('name')
    return render(request, 'index.html', {'products': products})

def product_details(request,pk):
    """Display product details page"""
    product = get_object_or_404(Product, pk=pk)
    bids = get_object_or_404(Bid, pk=pk)
    print(bids.bid)
    product.views += 1
    product.save()
    args = {'products':product,'bids':bids}
    return render(request, 'product_details.html', args)
