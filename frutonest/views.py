from django.shortcuts import render
from product.models import Product
from promotions.models import Deal
from about.models import TeamMember
from news.models import NewsArticle
from django.core.paginator import Paginator
import datetime




def home(request):
    # Fetch current deals
    current_date = datetime.date.today()
    deals = Deal.objects.filter(start_date__lte=current_date, end_date__gte=current_date).select_related('product')

    # Fetch products (optional, if you need to show all products as well)
    products = Product.objects.all()
    articles = NewsArticle.objects.all()
    deal_data = []
    for deal in deals:
        original_price = float(deal.product.price)
        discount_percentage = int(deal.discount_percentage)
        discounted_price = original_price * (1 - discount_percentage / 100.0)
        deal_data.append({
            'deal': deal,
            'discounted_price': discounted_price
        })

    return render(request, 'home.html', {
        'deals': deal_data,
        'products': products,
        'articles': articles,
    })

def home2(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'home2.html', context)



def shop(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'shop.html', context)

def page_not_found(request):
    return render(request, '404.html')
