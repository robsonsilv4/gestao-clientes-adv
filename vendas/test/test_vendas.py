from django.test import TestCase
from vendas.models import Venda


class VendaTestCase(TestCase):
    def setUp(self):
        Venda.objects.create(numero='123')

    def test_verifica_numero_vendas(self):
        assert Venda.objects.all().count() == 2
