from django.urls import path
from . import views

urlpatterns = [
    path('states/', views.StateCreateListView.as_view(), name='state-create-list'),
    path('states/<int:pk>/', views.StateRetrieveUpdateDestroyView.as_view(), name='state-detail-view'),
]
