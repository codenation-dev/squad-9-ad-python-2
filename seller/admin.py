from django.contrib import admin

from seller.models import Seller, Address
class AddressAdmin(admin.ModelAdmin):
    # Exibir colunas para a tabela Aulas no admin
    list_display = ['street', 'number', 'complement', 'city', 'state', 'country']

    # Set campos de pesquisa
    search_fields = ['state', 'city']

    # Filtro lateral
    list_filter = ['state', 'city']


class SellerAdmin(admin.ModelAdmin):
    # Exibir colunas para a tabela Courses no admin
    list_display = ['cpf', 'name', 'last_name', 'age', 'email', 'phone']

    # Set campos de pesquisa
    search_fields = ['cpf', 'name', 'age']

    # # Preencher o campo slug com os valores do campo nome
    # prepopulated_fields = {'slug': ('name',)}

    # Filtro lateral
    list_filter = ['age']


# Register your models here.
admin.site.register(Address, AddressAdmin)
admin.site.register(Seller, SellerAdmin)
