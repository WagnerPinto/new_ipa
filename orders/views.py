from rest_framework import generics, views, response, status
from django.db.models import F
from django.db.models.aggregates import Sum
from app.permissions import GlobalDefaultPermission
from . models import Order
from . serializers import OrderSerializer, OrderListDetailSerializer
from items_orders.models import OrderItem
from rest_framework.permissions import IsAuthenticated


class OrderCreateListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderListDetailSerializer
        return OrderSerializer


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderListDetailSerializer
        return OrderSerializer


class OrderStatsView(views.APIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Order.objects.all()

    def get(self, request):

        total_orders = self.queryset.count()
        orders_by_supplier = self.queryset.aggregate(total=Sum(F('order_amount')))['total']
        total_by_supplier = self.queryset.order_by('order_supplier_id').aggregate(total=Sum(F('order_amount')))['total']
        average_amount = OrderItem.objects.aggregate(avg_subtotal=Sum(F('unit_price') * F('quantity')))['avg_subtotal']

        return response.Response(
            data={'total_orders': total_orders,
                  'orders_by_supplier': orders_by_supplier,
                  'total_by_supplier': total_by_supplier,
                  'average_subtotal': average_amount,
                  },
            status=status.HTTP_200_OK,
        )
