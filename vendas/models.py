from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from produtos.models import Produto
from clientes.models import Pessoa


class Venda(models.Model):
    numero = models.IntegerField(unique=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    imposto = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)

    # def get_total(self):
    #     total = 0
    #     for produto in self.produtos.all():
    #         total += produto.preco
    #     return (total - self.desconto) - self.imposto

    def __str__(self):
        return str(self.numero)


class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.venda.numero) + ' - ' + self.produto.descricao


# @receiver(m2m_changed, sender=Venda.produtos.through)
def update_vendas_total(sender, instance, **kwargs):
    instance.valor = instance.get_total()
    instance.save()
    # total = instance.get_total()
    # Venda.objects.filter(id=instance.id).update(valor=total)
