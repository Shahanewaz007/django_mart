from django.shortcuts import render, redirect 
from .forms import RegistationForm
from django.contrib.auth import login, logout, authenticate
from cart.models import Cart, CartItem
# Create your views here.

def get_session_id(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def register(request):
    form = RegistationForm()
    if request.method == 'POST':
        form = RegistationForm(request.POST)
        if form.is_valid():
            user = form.save()
            session_key = get_session_id(request)
            cart = Cart.objects.get(cart_id = session_key)
            cart_item_exist = CartItem.objects.filter(cart=cart).exists()
            if cart_item_exist:
                cart_item = CartItem.objects.get(cart=cart)
                for item in cart_item:
                    item.user = user
            login(request, user)
            return redirect('cart')
    
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        login(request, user)
        return redirect('profile')
    return render(request, 'accounts/signin.html')



def user_logout(request):
    logout(request)
    return redirect('login')