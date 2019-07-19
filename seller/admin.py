from django.contrib import admin

from seller.models import Seller, Address, Telephone


class TelephoneInlineAdmin(admin.StackedInline):
    model = Telephone


class TelephoneAdmin(admin.ModelAdmin):

    # Exibir colunas para a tabela Courses no admin
    list_display = ["ddd", "phone_number"]

    # Set campos de pesquisa
    search_fields = ["ddd", "phone_number"]

    # Filtro lateral
    list_filter = ["ddd", ]


class AddressAdmin(admin.ModelAdmin):
    # Exibir colunas para a tabela Aulas no admin
    list_display = ['street', 'number', "complement", "city", "state", "country"]

    # Set campos de pesquisa
    search_fields = ['state', 'city']

    # Filtro lateral
    list_filter = ['state', 'city']


class SellerAdmin(admin.ModelAdmin):
    # Exibir colunas para a tabela Courses no admin
    list_display = ["cpf", "name", "last_name", "age", "email"]

    # Set campos de pesquisa
    search_fields = ['cpf', 'name', 'age']

    # # Preencher o campo slug com os valores do campo nome
    # prepopulated_fields = {'slug': ('name',)}

    # Filtro lateral
    list_filter = ["age",]
    inlines = [TelephoneInlineAdmin]


# Register your models here.
admin.site.register(Address, AddressAdmin)
admin.site.register(Telephone, TelephoneAdmin)
admin.site.register(Seller, SellerAdmin)
