from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartListCreateView(ListCreateAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartItemListCreateView(ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        serializer.save(cart= cart)


class CartItemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)
         