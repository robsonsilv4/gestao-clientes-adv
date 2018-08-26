from django.urls import path
from .views import DashboardView, NovaVenda, NovoItemPedido, ListaVendas

urlpatterns = [
    path('', ListaVendas.as_view(), name='lista-vendas'),
    path('nova-venda/', NovaVenda.as_view(), name='nova-venda'),
    path('nova-item-pedido/', NovoItemPedido.as_view(), name='novo-item-pedido'),
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]
