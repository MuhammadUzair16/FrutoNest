from django.contrib import admin
from .models import Product, Deal

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price')

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'discount_percentage', 'start_date', 'end_date')
    list_filter = ('product', 'start_date', 'end_date')
    search_fields = ('name', 'description', 'product__product_name')
