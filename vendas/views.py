from django.shortcuts import render
from django.views import View
from .models import Venda, ItemDoPedido
from django.db.models import F, Sum, Avg, Min, Max, Count


class DashboardView(View):
    def get(self, request):
        data = {'media': Venda.objects.all().aggregate(Avg('valor'))['valor__avg'],
                'media_desc': Venda.objects.all().aggregate(Avg('desconto'))['desconto__avg'],
                'min': Venda.objects.all().aggregate(Min('valor'))['valor__min'],
                'total': Venda.objects.all().aggregate(Count('id'))['id__count'],
                'total_nfe': Venda.objects.filter(nfe_emitida=True).aggregate(Count('id'))['id__count']}
        return render(request, 'vendas/dashboard.html', data)
