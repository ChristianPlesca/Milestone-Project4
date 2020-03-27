from django.shortcuts import render
from products.models import Product
from django.db.models import Q

def search(request):
    products = Product.objects.all()
    query = request.GET.get("q")
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(bid_price__icontains=query)).distinct()
    return render(request, 'index.html' ,{"products":products})