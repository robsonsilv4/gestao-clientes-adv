from django.shortcuts import render, redirect, HttpResponse
from django.views import View

from .models import Venda, ItemDoPedido
from .forms import ItemDoPedidoForm


class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Você não tem as permissões necessárias')

        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = {'media': Venda.objects.media,
                'media_desc': Venda.objects.media_desconto,
                'venda_min': Venda.objects.venda_min,
                'venda_max': Venda.objects.venda_max,
                'ped_total': Venda.objects.pedido_total,
                'ped_tot_nfe': Venda.objects.pedido_total_nfe}
        return render(request, 'vendas/dashboard.html', data)


class NovaVenda(View):
    def get(self, request):
        return render(request, 'vendas/nova-venda.html')

    def post(self, request):
        data = {'form_item': ItemDoPedidoForm(),
                'numero': request.POST['numero'],
                'desconto': float(request.POST['desconto'].replace(',', '.')),
                'venda_id': request.POST['venda_id']}

        if data['venda_id']:
            venda = Venda.objects.get(id=data['venda_id'])
            venda.desconto = ['desconto']
            venda.numero = data['numero']
            venda.save()
        else:
            venda = Venda.objects.create(
                numero=data['numero'],
                desconto=data['desconto']
            )

        itens = venda.itemdopedido_set.all()
        data['venda'] = venda
        data['itens'] = itens

        return render(request, 'vendas/nova-venda.html', data)


class NovoItemPedido(View):
    def get(self, request, pk):
        pass

    def post(self, request, venda):
        data = {}
        item = ItemDoPedido.objects.create(
            produto_id=request.POST['produto_id'],
            quantidade=request.POST['quantidade'],
            desconto=request.POST['desconto'],
            venda_id=venda
        )

        data['item'] = item
        data['form_item'] = ItemDoPedidoForm()
        data['numero'] = item.venda.numero
        data['desconto'] = item.venda.desconto
        data['venda'] = item.venda
        data['itens'] = item.venda.itemdopedido_set.all()

        return render(request, 'vendas/nova-venda', data)


class ListaVendas(View):
    def get(self, request):
        vendas = Venda.objects.all()
        count_vendas = vendas.count()
        return render(request, 'vendas/lista-vendas.html',
                      {'vendas': vendas, 'count_vendas': count_vendas})


class EditPedido(View):
    def get(self, request, venda):
        data = {}
        venda = Venda.objects.get(id=venda)
        data['form_item'] = ItemDoPedidoForm()
        data['numero'] = venda.numero
        data['desconto'] = float(venda.desconto)
        data['venda'] = venda
        data['itens'] = venda.itemdopedido_set.all()
        return render(request, 'vendas/nova-venda.html', data)


class DeletePedido(View):
    def get(self, request, venda):
        venda = Venda.objects.get(id=venda)
        return render(request,
                      'vendas/delete-pedido-confirm.html',
                      {'venda': venda})

    def post(self, request, venda):
        venda = Venda.objects.get(id=venda)
        venda.delete()
        return redirect('lista-vendas')


class DeleteItemPedido(View):
    def get(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        return render(request,
                      'vendas/delete-item-pedido-confirm.html',
                      {'item_pedido': item_pedido})

    def post(self, request, item):
        item_pedido = Venda.objects.get(id=item)
        venda_id = item_pedido.venda.id
        item_pedido.delete()
        return redirect('edit-pedido', venda=venda_id)
