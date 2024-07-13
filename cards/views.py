from rest_framework import generics
from app.permissions import GlobalDefaultPermission
from .models import Card
from .serializers import CardSerializer
from rest_framework.permissions import IsAuthenticated

class CardCreateListView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    
class CardRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
