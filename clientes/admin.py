from django.contrib import admin
from .models import Pessoa, Documento, Produto, Venda

admin.site.register(Pessoa)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)