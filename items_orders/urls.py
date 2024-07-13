from django.urls import path
from . import views

urlpatterns = [
    path('items_orders/', views.ItemOrderCreateListView.as_view(), name='item_order-create-list'),
    path('items_orders/<int:pk>/', views.ItemOrderRetrieveUpdateDestroyViem.as_view(), name='item_order-detail-view'),
]