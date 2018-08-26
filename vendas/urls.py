from django.urls import path
from .views import DashboardView, NovaVenda, NovoItemPedido, ListaVendas, EditPedido, DeletePedido, DeleteItemPedido

urlpatterns = [
    path(
        '',
        ListaVendas.as_view(),
        name='lista-vendas'),
    path(
        'nova-venda/',
        NovaVenda.as_view(),
        name='nova-venda'),
    path(
        'novo_item_pedido/<int:venda>/',
        NovoItemPedido.as_view(),
        name='novo-item-pedido'),
    path(
        'edit-pedido/<int:venda>/',
        EditPedido.as_view(),
        name='edit-pedido'),
    path(
        'delete_pedido/<int:venda>/',
        DeletePedido.as_view(),
        name='delete-pedido'),
    path(
        'delete_item_pedido/<int:item>/',
        DeleteItemPedido.as_view(),
        name='delete-item-pedido'),
    path(
        'dashboard/',
        DashboardView.as_view(),
        name='dashboard')]
