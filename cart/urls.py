from django.urls import path
from .views import CartListCreateView, CartItemListCreateView


urlpatterns = [
    path('cart/', CartListCreateView.as_view(), name='cart'),
    path('cart/items/', CartItemListCreateView.as_view(), name='Cart_items'),
]
