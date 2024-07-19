from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from cart.models import Cart, CartItem
from product.models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1,
        )
        cart_item.save()

    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    shipping = 50
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        cart_items = []

    grand_total = total + shipping  # Calculate grand total

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'shipping': shipping,
        'grand_total': grand_total,
    }
    return render(request, 'product/cart.html', context)


@csrf_exempt
def update_cart_item_quantity(request):
    if request.method == 'POST':
        item_ids = request.POST.getlist('item_ids[]')
        quantities = request.POST.getlist('quantities[]')

        for item_id, quantity in zip(item_ids, quantities):
            try:
                cart_item = get_object_or_404(CartItem, id=item_id)
                cart_item.quantity = quantity
                cart_item.save()
            except CartItem.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': f'Item with id {item_id} not found'})

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@csrf_exempt
def remove_cart_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        try:
            cart_item = get_object_or_404(CartItem, id=item_id)
            cart_item.delete()
            return JsonResponse({'status': 'success'})
        except CartItem.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Item not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def checkout(request):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        total = 0
        for cart_item in cart_items:
            cart_item.total_price = cart_item.product.price * cart_item.quantity
            total += cart_item.total_price
        shipping = 50
        grand_total = total + shipping
    except ObjectDoesNotExist:
        cart_items = []
        total = 0
        shipping = 50
        grand_total = shipping

    context = {
        'cart_items': cart_items,
        'total': total,
        'shipping': shipping,
        'grand_total': grand_total,
    }
    return render(request, 'checkout.html', context)
