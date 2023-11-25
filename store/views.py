from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import Paginator
# Create your views here.

def store(request, category_slug=None):
    products = None
    category = None
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_avaiable=True, category=category)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        page_product = paginator.get_page(page)
    else:  
        products = Product.objects.filter(is_avaiable = True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        page_product = paginator.get_page(page)
    
    categories = Category.objects.all()
    product = {'products':page_product, 'categories': categories}
    return render(request, 'store/store.html',product)


def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
    
    return render(request, 'store/product_detail.html', {'product':single_product})