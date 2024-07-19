from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('update-cart-item-quantity/', views.update_cart_item_quantity, name='update_cart_item_quantity'),
    path('remove-cart-item/', views.remove_cart_item, name='remove_cart_item'),
    path('checkout/', views.checkout, name='checkout'),


]