from django.db import models
from product.models import Product
from promotions.models import Deal

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    deal = models.ForeignKey(Deal, null=True, blank=True, on_delete=models.SET_NULL)

    def price(self):
        base_price = self.product.price
        if self.deal:
            return base_price * (1 - self.deal.discount_percentage / 100)
        return base_price

    def __str__(self):
        return str(self.product)



