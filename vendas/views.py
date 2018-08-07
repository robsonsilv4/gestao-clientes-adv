from django.shortcuts import render
from django.views import View

from .models import Venda


class DashboardView(View):
    def get(self, request):
        data = {'media': Venda.objects.media,
                'media_desc': Venda.objects.media_desconto,
                'venda_min': Venda.objects.venda_min,
                'venda_max': Venda.objects.venda_max,
                'ped_total': Venda.objects.pedido_total,
                'ped_tot_nfe': Venda.objects.pedido_total_nfe}
        return render(request, 'vendas/dashboard.html', data)
