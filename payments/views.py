from rest_framework import generics
from app.permissions import GlobalDefaultPermission
from .models import Payment
from .serializers import PaymentSerializer, PaymentListDetailSerializer
from rest_framework.permissions import IsAuthenticated


class PaymentCreateListView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PaymentListDetailSerializer
        return PaymentSerializer


class PaymentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PaymentListDetailSerializer
        return PaymentSerializer
