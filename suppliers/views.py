from rest_framework import generics
from app.permissions import GlobalDefaultPermission
from . models import Supplier
from . serializers import SupplierSerializer
from rest_framework.permissions import IsAuthenticated


class SupplierCreateListView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)


class SupplierRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
