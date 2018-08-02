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
    list_display = ['first_name', 'last_name', 'age', 'salary', 'photo']


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)
