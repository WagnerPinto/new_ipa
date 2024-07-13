from rest_framework import generics
from app.permissions import GlobalDefaultPermission
from . models import Product
from . serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated


class ProductCreateListView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
