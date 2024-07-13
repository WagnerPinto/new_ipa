from django.urls import path
from . import views

urlpatterns = [
    path('banks/', views.BankCreateListView.as_view(), name='bank-create-list'),
    path('banks/<int:pk>/', views.BankRetrieveUpdateDestroyView.as_view(), name='bank-detail-view'),
]
