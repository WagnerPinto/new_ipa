from rest_framework import serializers
from . models import ExpenseAccount

class ExpenseAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseAccount
        fields = '__all__'