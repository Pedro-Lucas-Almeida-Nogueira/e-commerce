from rest_framework.generics import ListAPIView
from .models import Cart
from .serializers import CartSerializer

class CartListView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
