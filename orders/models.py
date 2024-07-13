from django.db import models
from django.db.models.aggregates import Sum
from django.db.models import F
from suppliers.models import Supplier

class Order(models.Model):
    
    order_number = models.CharField(max_length=12)
    order_date = models.DateField()
    order_supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='suppliers')
    order_amount = models.DecimalField(max_digits=12, decimal_places=2)
    
    @property
    def total(self):
        queryset = self.orders.all().aggregate(total=models.Sum(F('quantity') * F('unit_price'))
        )
        return queryset['total']
        
    
    
    def __str__(self):
        return self.order_number