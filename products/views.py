from django.shortcuts import render
from .models import Product,ProductsPictures
from django.core import serializers

def home_page(request):
    """Display index page"""
    products = Product.objects.all()
    product_images = ProductsPictures.objects.all()
    json_serializer = serializers.get_serializer("json")()
    query_results = json_serializer.serialize( Product.objects.all(), ensure_ascii=False )
    return render(request, 'index.html', {'products': products, 'product_images':product_images,'query_results':query_results})
