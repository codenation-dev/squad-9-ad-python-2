from django.contrib import admin

from notifications.models import Notification


class NotificationAdmin(admin.ModelAdmin):
    # Exibir colunas para a tabela Courses no admin
    list_display = ["average_sales", "seller"]
    # Set campos de pesquisa
    search_fields = ['average_sales', 'seller']


# Register your models here.
admin.site.register(Notification, NotificationAdmin)
