from django.urls import path
from . import views

urlpatterns = [
    path('cards/', views.CardCreateListView.as_view(), name='card-create-list'),
    path('cards/<int:pk>/', views.CardRetrieveUpdateDestroy.as_view(), name='card-detail-view'),
]
