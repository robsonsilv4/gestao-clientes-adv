from django.contrib import admin
from .models import Pessoa, Documento, Produto, Venda


class PessoaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados Pessoais', {'fields': ('first_name', 'last_name', 'num_doc')}),
        ('Dados Complementares', {'classes': ('collapse',),
                                  'fields': ('age', 'salary', 'photo')})
    )

    # fields = [('first_name', 'last_name'), ('age', 'salary'), 'bio', 'photo']
    # exclude = ['bio']

    list_filter = ('age', 'salary')

    list_display = ['first_name', 'last_name', 'age', 'salary', 'tem_foto']

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'

    tem_foto.short_description = 'Possui Foto'


class VendaAdmin(admin.ModelAdmin):
    raw_id_fields = ('pessoa',)
    readonly_fields = ('valor',)
    list_filter = ('pessoa__num_doc', 'desconto')
    list_display = ('id', 'pessoa', 'total')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__num_doc__num_doc')

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'


class ProdutoAdmin(admin.ModelAdmin):
    list_filter = ('preco',)


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
