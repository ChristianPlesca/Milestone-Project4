from django.shortcuts import render
from .models import Product,ProductsPictures

def home_page(request):
    """Display index page"""
    products = Product.objects.all()
    product_images = ProductsPictures.objects.all()
    return render(request, 'index.html', {'products': products, 'product_images':product_images})
