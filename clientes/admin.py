from django.contrib import admin
from .models import Pessoa, Documento, Produto, Venda


class PessoaAdmin(admin.ModelAdmin):
    # fields = ['first_name', 'last_name', 'age', 'salary']
    exclude = ['bio']
    list_display = ['id', 'first_name', 'last_name', 'age', 'salary', 'photo']


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)
