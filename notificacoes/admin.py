from django.contrib import admin

from notificacoes.models import Notificacoes


class NotificacoesAdmin(admin.ModelAdmin):

    # Exibir colunas para a tabela Courses no admin
    list_display = ["media_venda", "vendedor"]

    # Set campos de pesquisa
    search_fields = ['media_venda', 'vendedor']


# Register your models here.
admin.site.register(Notificacoes, NotificacoesAdmin)
