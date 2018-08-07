from django.http import HttpResponseNotFound


def emitir_nfe(modeladmin, request, queryset):
    if not request.user.has_perm('vendas.setar_nfe'):
        return HttpResponseNotFound('<h1>Sem permissão</h1>')
    else:
        queryset.update(nfe_emitida=True)


def cancelar_nfe(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)


emitir_nfe.short_description = 'Emitir todas notas fiscais'
cancelar_nfe.short_description = 'Cancelar notas fiscais emitidas'
