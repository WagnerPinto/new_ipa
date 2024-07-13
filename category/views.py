from rest_framework import generics
from app.permissions import GlobalDefaultPermission
from . models import Category
from . serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated

class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
