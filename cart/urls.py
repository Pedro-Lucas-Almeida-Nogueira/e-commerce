from django.urls import path
from .views import CartListCreateView, CartItemListCreateView, CartItemDetailView


urlpatterns = [
    path('cart/', CartListCreateView.as_view(), name='cart'),
    path('cart/items/', CartItemListCreateView.as_view(), name='cart_items'),
    path('cart/items/<int:id>/', CartItemDetailView.as_view(), name= 'cart_item'),
]
