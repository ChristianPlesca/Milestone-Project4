from django.shortcuts import render

def home_page(request):
    """Display index page"""
    return render(request,'index.html')
