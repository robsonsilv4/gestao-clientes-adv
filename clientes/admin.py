from django.contrib import admin
from .models import Pessoa, Documento


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
    search_fields = ['id', 'first_name']

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'

    tem_foto.short_description = 'Possui Foto'


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Documento)
