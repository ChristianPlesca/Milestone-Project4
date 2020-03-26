from django.shortcuts import render
from products.models import Product
from django.db.models import Q


def search(request):
    products = Product.objects.all()
    query = request.GET.get("q")
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(initial_price__icontains=query) |
            Q(bid_price__icontains=query)).distinct()
    return render(request, 'index.html' ,{"products":products})

def sort_by_max_price(request):
   product = Product.objects.all().order_by('price')
   return render(request, 'index.html', {"product": product})
   
def sort_by_min_price(request):
   product = Product.objects.all().order_by('-price')
   return render(request, 'index.html', {"product": product})
