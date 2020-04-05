from django.shortcuts import render,get_object_or_404
from .models import Product,ProductsPictures

def home_page(request):
    """Display index page"""
    products = Product.objects.all()
    product_pictures = ProductsPictures.objects.all()
    return render(request, 'index.html', {'products': products,'product_pictures':product_pictures})

def product_details(request,pk):
    """Display product details page"""
    product = get_object_or_404(Product, pk=pk)
    return render(request,'product_details.html', {'product':product})
