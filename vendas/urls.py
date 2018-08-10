from django.urls import path
from .views import DashboardView, NovaVenda

urlpatterns = [
    path('nova-venda/', NovaVenda.as_view(), name='nova-venda'),
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]
