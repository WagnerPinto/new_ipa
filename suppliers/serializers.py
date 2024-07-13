from rest_framework import serializers
from . models import Supplier
from states.serializers import StateSerializer


class SupplierSerializer(serializers.ModelSerializer):
    
    state = StateSerializer()
    
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'cnpj', 'city', 'state' ]
