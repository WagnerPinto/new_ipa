from rest_framework import serializers
from . models import Affiliate

class AffiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliate
        fields = '__all__'