from django.contrib import admin

from product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'image', 'modified_at', 'is_available')


admin.site.register(Product)