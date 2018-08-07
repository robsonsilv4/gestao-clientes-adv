from django.db import models
from django.db.models import Avg, Min, Max, Count


class VendaManager(models.Manager):
    def media(self):
        return self.all().aggregate(Avg('valor'))['valor__avg']

    def media_desconto(self):
        return self.all().aggregate(Avg('desconto'))['desconto__avg']

    def venda_min(self):
        return self.all().aggregate(Min('valor'))['valor__min']

    def venda_max(self):
        return self.all().aggregate(Max('valor'))['valor__max']

    def pedido_total(self):
        return self.all().aggregate(Count('id'))['id__count']

    def pedido_total_nfe(self):
        return self.filter(nfe_emitida=True).aggregate(Count('id'))['id__count']
