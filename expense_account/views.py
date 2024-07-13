from rest_framework import generics
from app.permissions import GlobalDefaultPermission
from . models import ExpenseAccount
from . serializers import ExpenseAccountSerializer
from rest_framework.permissions import IsAuthenticated

class ExpenseAccountCreateListView(generics.ListCreateAPIView):
    queryset = ExpenseAccount.objects.all()
    serializer_class = ExpenseAccountSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    
class ExpenseAccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpenseAccount.objects.all()
    serializer_class = ExpenseAccountSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)