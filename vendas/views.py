from django.shortcuts import render
from django.views import View
from .models import Venda, ItemDoPedido
from django.db.models import F, Sum, Avg, Max, FloatField


class DashboardView(View):
    def get(self, request):
        media = Venda.objects.all().aggregate(Avg('valor'))['valor__avg']
        return render(request, 'vendas/dashboard.html', {'media': media})
