from django.shortcuts import render, HttpResponse
from django.views import View

from .models import Venda


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
        data = {'numero': request.POST['numero'],
                'desconto': float(request.POST['numero']),
                'venda': request.POST['venda_id']}

        if data['venda']:
            venda = Venda.objects.get(id=data['venda'])
        else:
            venda = Venda.objects.create(
                numero=data['numero'],
                desconto=data['desconto']
            )

        itens = venda.itemdopedido_set.all()
        data['venda_obj'] = venda
        data['itens'] = itens

        return render(request, 'vendas/nova-venda.html', data)
