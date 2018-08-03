from django.contrib import admin
from .models import Venda, ItemDoPedido
from .actions import emitir_nfe, cancelar_nfe


# TabularInline/StackedInline
class ItemDoPedidoInline(admin.TabularInline):
    model = ItemDoPedido
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    list_filter = ('pessoa__num_doc', 'desconto')
    list_display = ('id', 'pessoa', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__num_doc__num_doc')
    actions = [emitir_nfe, cancelar_nfe]
    autocomplete_fields = ['pessoa']
    inlines = [ItemDoPedidoInline]

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido)
