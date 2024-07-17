from django.shortcuts import render
from product.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'home.html', context)

def home2(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'home2.html', context)

def about(request):
  return render(request, 'about.html')