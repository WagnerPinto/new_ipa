from rest_framework import generics
from app.permissions import GlobalDefaultPermission
from . models import Expense
from . serializers import ExpenseSerializer
from rest_framework.permissions import IsAuthenticated

class ExpenseCreateListView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    
class ExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)