from django.shortcuts import render
from .models import Product

def home_page(request):
    """Display index page"""
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
