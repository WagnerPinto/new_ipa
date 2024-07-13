from rest_framework import serializers
from . models import Order
from django.db.models.aggregates import Sum
from items_orders.models import OrderItem
from suppliers.serializers import SupplierSerializer

class OrderSerializer(serializers.ModelSerializer):
    
    total = serializers.SerializerMethodField()
    
    def get_total(self, obj):
        return obj.total
    
    
    class Meta:
        model = Order
        fields = ('id', 'order_number', 'order_date','order_supplier', 'order_amount', 'total')

class OrderListDetailSerializer(serializers.ModelSerializer):
    
    order_supplier = SupplierSerializer()
    
    total = serializers.SerializerMethodField()
    
    def get_total(self, obj):
        return obj.total
    
    class Meta:
        model = Order
        fields = ['id', 'order_number', 'order_date', 'order_supplier', 'order_amount', 'total']
    