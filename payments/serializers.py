from rest_framework import serializers
from .models import Payment
from orders.serializers import OrderListDetailSerializer
from banks.serializers import BankSerializer
from cards.serializers import CardSerializer
from expenses.serializers import ExpenseSerializer


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        
class PaymentListDetailSerializer(serializers.ModelSerializer):
    
     payment_order = OrderListDetailSerializer()
     payment_bank = BankSerializer()
     payment_card = CardSerializer()
     payment_expense = ExpenseSerializer()
     
     class Meta:
         model = Payment
         fields = '__all__'