from rest_framework import serializers
from . models import Expense
from affiliates.serializers import AffiliateSerializer
from expense_account.serializers import ExpenseAccountSerializer
from suppliers.serializers import SupplierSerializer

class ExpenseSerializer(serializers.ModelSerializer):
    account = ExpenseAccountSerializer()
    supplier = SupplierSerializer()
    center_cost = AffiliateSerializer()
    
    class Meta:
        model = Expense
        fields = '__all__'