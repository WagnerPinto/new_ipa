from django.urls import path
from . import views

urlpatterns = [
    path('expense_account/', views.ExpenseAccountCreateListView.as_view(), name='expense_account-create-list'),
    path('expense_account/<int:pk>/', views.ExpenseAccountRetrieveUpdateDestroyView.as_view(), name='expense_account-detail-view'),
]

