from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product_detail.html', {'product': product})