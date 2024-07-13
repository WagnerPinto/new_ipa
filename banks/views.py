from rest_framework import generics
from app.permissions import GlobalDefaultPermission
from .models import Bank
from .serializers import BankSerializer
from rest_framework.permissions import IsAuthenticated

class BankCreateListView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    
class BankRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
