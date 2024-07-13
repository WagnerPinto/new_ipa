from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderCreateListView.as_view(), name='order-create-list'),
    path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order-detail-view'),
    path('orders/stats/', views.OrderStatsView.as_view(), name='order-stats-view'),
]
