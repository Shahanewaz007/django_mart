from django.shortcuts import render
from store.models import Product

def home(request):
    product = Product.objects.filter(is_avaiable = True)
    
    return render(request, 'index.html', {'products': product})