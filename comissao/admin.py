from django.contrib import admin

from comissao.models import Comissao


class ComissaoAdmin(admin.ModelAdmin):
    # Exibir colunas para a tabela Courses no admin
    list_display = ["nome", "porcentagem_menor", "porcentagem_maior", "valor_minimo"]

    # Set campos de pesquisa
    search_fields = ['vendedor', 'nome']

    # Filtro lateral
    list_filter = ["porcentagem_menor", "porcentagem_maior", "nome"]


# Register your models here.
admin.site.register(Comissao, ComissaoAdmin)

