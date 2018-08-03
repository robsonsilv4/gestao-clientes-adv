def emitir_nfe(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)


def cancelar_nfe(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)


emitir_nfe.short_description = 'Emitir todas notas fiscais'
cancelar_nfe.short_description = 'Cancelar notas fiscais emitidas'
