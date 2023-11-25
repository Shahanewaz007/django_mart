from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartItem
# Create your views here.

def get_session_id(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def cart(request):
    cart_items = None
    total = 0
    tax = 0
    grand_total = 0
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user = request.user)
        for item in cart_items:
            total += item.product.price * item.quantity
    else:
        session_id = get_session_id(request)
        cart_id = Cart.objects.filter(cart_id = session_id).exists()
        if cart_id:
            cart_model = Cart.objects.get(cart_id = session_id)
            cart_items = CartItem.objects.filter(cart = cart_model)
            for item in cart_items:
                total += item.product.price * item.quantity
    tax = (5*total)/100
    grand_total = total + tax
    
    return render(request, 'cart/cart.html', {'cart_items':cart_items, 'total' : total, 'tax':tax, 'grand_total': grand_total})


        
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    session_id = get_session_id(request)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(product=product, user=request.user).exists()
        if cart_item:
            item = CartItem.objects.get(product=product,user=request.user)
            item.quantity += 1
            item.save()
        else:
            item = CartItem.objects.create(
            product = product,
            quantity = 1,
            user = request.user
            )
            item.save()
    else:
        cart_id = Cart.objects.filter(cart_id=session_id).exists()
        if cart_id:
            cart_item = CartItem.objects.filter(product=product).exists()
            if cart_item:
                item = CartItem.objects.get(product=product)
                item.quantity += 1
                item.save()
            else:
                cartid = Cart.objects.get(cart_id=session_id)
                item = CartItem.objects.create(
                product = product,
                cart = cartid,
                quantity = 1,
                )
                item.save()
                
        else:
            cart = Cart.objects.create(cart_id=session_id,)
            cart.save()
            cart_item = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1,
            )
            cart_item.save()

    return redirect('cart')


def minus_item(request, product_id):
    product = Product.objects.get(id = product_id)
    if request.user.is_authenticated:
        cartitem = CartItem.objects.get(user=request.user, product=product)
    else:
        session_id = get_session_id(request)
        cart_model = Cart.objects.get(cart_id = session_id)
        cartitem = CartItem.objects.get(cart=cart_model, product=product)
    
    if cartitem.quantity > 1:
        cartitem.quantity -= 1
        cartitem.save()
    else:
        cartitem.delete()
    return redirect('cart')

def remove_cart_item(request, product_id):
    product = Product.objects.get(id = product_id)
    if request.user.is_authenticated:
        cartitem = CartItem.objects.get(user=request.user, product=product)
    else:
        session_id = get_session_id(request)
        cart_model = Cart.objects.get(cart_id = session_id)
        cartitem = CartItem.objects.get(cart=cart_model, product=product)
    
    if cartitem:
        cartitem.delete()
    
    return redirect('cart')
    