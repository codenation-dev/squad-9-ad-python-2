from django.contrib import admin

from notificacoes.models import Notificacoes


class NotificacoesAdmin(admin.ModelAdmin):

    # Exibir colunas para a tabela Courses no admin
    list_display = ["media_venda", "seller"]

    # Set campos de pesquisa
    search_fields = ['media_venda', 'seller']


# Register your models here.
admin.site.register(Notificacoes, NotificacoesAdmin)
