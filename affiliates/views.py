from rest_framework import generics
from app.permissions import GlobalDefaultPermission
from rest_framework.permissions import IsAuthenticated
from .models import Affiliate
from .serializers import AffiliateSerializer


class AffiliateCreateListView(generics.ListCreateAPIView):
    queryset = Affiliate.objects.all()
    serializer_class = AffiliateSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    
class AffiliateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Affiliate.objects.all()
    serializer_class = AffiliateSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
