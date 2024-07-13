from rest_framework import serializers
from . models import OrderItem
from products.serializers import ProductSerializer
from django.db.models.aggregates import Sum
from orders.serializers import OrderListDetailSerializer



class OrderItemSerializer(serializers.ModelSerializer):
    
    product = ProductSerializer()
    subtotal = serializers.SerializerMethodField()
   
        
    def get_subtotal(self, obj):
        
        return obj.subtotal
    
    
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'quantity', 'unit_price', 'subtotal')
        
class OrderItemListDetailSerializer(serializers.ModelSerializer):
    
   
    product = ProductSerializer()
    subtotal = serializers.SerializerMethodField()
   
        
    def get_subtotal(self, obj):
        
        return obj.subtotal
    
    
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'quantity', 'unit_price', 'subtotal')
        
        
    
         
        