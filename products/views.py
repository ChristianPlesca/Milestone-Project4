from django.shortcuts import render,get_object_or_404
from .models import Product, ProductsPictures
from bid.models import ProductBid , Bid

def home_page(request):
    """Displays index page"""
    products = Product.objects.all().order_by('name')
    return render(request, 'index.html', {'products': products})

def product_details(request,pk):
    """Gets the product ID and displays the specific product selected in products_details.html"""
    product = get_object_or_404(Product, pk=pk)
    product.views += 1
    product.save()
    args = {'product':product}
    return render(request, 'product_details.html', args)


