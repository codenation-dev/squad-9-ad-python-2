from django.contrib import admin

from vendas.models import Vendas


class VendasAdmin(admin.ModelAdmin):
    # Exibir colunas para a tabela Courses no admin
    list_display = ["month", "amount", "seller"]

    # Set campos de pesquisa
    search_fields = ['month', 'nome', 'idade']

    # # Preencher o campo slug com os valores do campo nome
    # prepopulated_fields = {'slug': ('name',)}

    # Filtro lateral
    list_filter = ["month", ]


# Register your models here.
admin.site.register(Vendas, VendasAdmin)
