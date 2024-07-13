from rest_framework import generics
from app.permissions import GlobalDefaultPermission
from . models import State
from . serializers import StateSerializer
from rest_framework.permissions import IsAuthenticated


class StateCreateListView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)


class StateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
