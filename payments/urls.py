from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.PaymentCreateListView.as_view(), name='payment-create-list'),
    path('payments/<int:pk>/', views.PaymentRetrieveUpdateDestroyView.as_view(), name='payment-detail-view'),
]
