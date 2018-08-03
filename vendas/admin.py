from django.contrib import admin
from .models import Venda, ItensDoPedido
from .actions import emitir_nfe, cancelar_nfe

class VendaAdmin(admin.ModelAdmin):
    # raw_id_fields = ('pessoa',)
    readonly_fields = ('valor',)
    list_filter = ('pessoa__num_doc', 'desconto')
    list_display = ('id', 'pessoa', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__num_doc__num_doc')
    actions = [emitir_nfe, cancelar_nfe]
    autocomplete_fields = ['pessoa']

    # filter_horizontal = ['produtos']
    # filter_vertical = ['produtos']

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'

admin.site.register(Venda, VendaAdmin)
admin.site.register(ItensDoPedido)