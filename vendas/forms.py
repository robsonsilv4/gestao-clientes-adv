from django import forms


class ItemDoPedidoForm(forms.Form):
    pedido_id = forms.CharField(label='ID do Produto', max_length=100)
    quantidade = forms.IntegerField(label='Quantidade')
    desconto = forms.DecimalField(label='Desconto', max_digits=7, decimal_places=2)
