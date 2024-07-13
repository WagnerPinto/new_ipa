from django.urls import path
from . import views

urlpatterns = [
    path('affiliates/', views.AffiliateCreateListView.as_view(), name='affiliate-create-list'),
    path('affiliate/<int:pk>/', views.AffiliateRetrieveUpdateDestroyView.as_view(), name='affiliate-detail-view'),
]
