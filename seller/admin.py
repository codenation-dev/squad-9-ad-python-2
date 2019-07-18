from django.contrib import admin

from vendedor.models import Vendedor, Endereco, Telefone


class TelefoneInlineAdmin(admin.StackedInline):
    model = Telefone


class TelefoneAdmin(admin.ModelAdmin):

    # Exibir colunas para a tabela Courses no admin
    list_display = ["ddd", "numero_telefone"]

    # Set campos de pesquisa
    search_fields = ["ddd", "numero_telefone"]

    # Filtro lateral
    list_filter = ["ddd", ]


class EnderecoAdmin(admin.ModelAdmin):
    # Exibir colunas para a tabela Aulas no admin
    list_display = ['logradouro', 'numero', "complemento", "cidade", "estado", "pais"]

    # Set campos de pesquisa
    search_fields = ['estado', 'cidade']

    # Filtro lateral
    list_filter = ['estado', 'cidade']


class VendedorAdmin(admin.ModelAdmin):
    # Exibir colunas para a tabela Courses no admin
    list_display = ["cpf", "nome", "sobrenome", "idade", "email"]

    # Set campos de pesquisa
    search_fields = ['cnpj', 'nome', 'idade']

    # # Preencher o campo slug com os valores do campo nome
    # prepopulated_fields = {'slug': ('name',)}

    # Filtro lateral
    list_filter = ["idade",]
    inlines = [TelefoneInlineAdmin]


# Register your models here.
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Vendedor, VendedorAdmin)
