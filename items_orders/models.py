from django.db import models
from orders.models import Order
from products.models import Product
from django.db.models.aggregates import Sum

class OrderItem(models.Model):
    
 order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='orders')
 product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='products')
 quantity = models.DecimalField(max_digits=12, decimal_places=3)
 unit_price = models.DecimalField(max_digits=12, decimal_places=2)
 
 @property
 def subtotal(self):
     return self.quantity * self.unit_price
 
 
 def total(self, obj):
     return OrderItem.objects.aggregate(Sum('self.subtotal'))
 
 
 
 def __str__(self):
     return str(self.order) 