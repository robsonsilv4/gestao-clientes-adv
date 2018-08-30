from django.test import TestCase
from gestao_clientes.vendas.models import Venda, ItemDoPedido
from gestao_clientes.produtos.models import Produto


class VendaTestCase(TestCase):
    def setUp(self):
        self.venda = Venda.objects.create(numero=123, desconto=10)
        self.produto = Produto.objects.create(
            descricao='Produto 1', preco=10)

    def test_numero_vendas(self):
        assert Venda.objects.all().count() == 1

    def test_valor_venda(self):
        ItemDoPedido.objects.create(
            venda=self.venda,
            produto=self.produto,
            quantidade=10,
            desconto=10)
        assert self.venda.valor == 80

    def test_desconto(self):
        assert self.venda.desconto == 10
