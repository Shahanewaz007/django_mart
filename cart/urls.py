from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart, name='cart'),
    path('<int:product_id>/', views.add_to_cart, name='add_cart'),
    path('minus/<int:product_id>/', views.minus_item, name='minus_item'),
    path('remove/<int:product_id>/', views.remove_cart_item, name='remove_item'),
]