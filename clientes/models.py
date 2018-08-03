from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class Documento(models.Model):
    num_doc = models.CharField(max_length=14)

    def __str__(self):
        return self.num_doc


class Pessoa(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clientes_photos', null=True, blank=True)
    num_doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    @property
    def nome_completo(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Produto(models.Model):
    descricao = models.CharField(max_length=45)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao


class Venda(models.Model):
    numero = models.IntegerField(unique=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    imposto = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, blank=True)
    nfe_emitida = models.BooleanField(default=False)

    def get_total(self):
        total = 0
        for produto in self.produtos.all():
            total += produto.preco
        return (total - self.desconto) - self.imposto

    def __str__(self):
        return str(self.numero)


@receiver(m2m_changed, sender=Venda.produtos.through)
def update_vendas_total(sender, instance, **kwargs):
    instance.valor = instance.get_total()
    instance.save()
    # total = instance.get_total()
    # Venda.objects.filter(id=instance.id).update(valor=total)
