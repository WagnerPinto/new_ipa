from rest_framework import generics
from app.permissions import GlobalDefaultPermission
from . models import OrderItem
from . serializers import OrderItemSerializer, OrderItemListDetailSerializer
from rest_framework.permissions import IsAuthenticated


class ItemOrderCreateListView(generics.ListCreateAPIView):
    
    queryset = OrderItem.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemListDetailSerializer
        return OrderItemSerializer
    
class ItemOrderRetrieveUpdateDestroyViem(generics.RetrieveUpdateDestroyAPIView):

    queryset = OrderItem.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemListDetailSerializer
        return OrderItemSerializer
    