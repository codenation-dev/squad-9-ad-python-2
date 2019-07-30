from django.db import models
from seller.models import Seller


class Notification(models.Model):
    """
        Modelo que representa as notificacoes do vendedor
    """

    seller = models.ForeignKey(
        Seller,
        verbose_name='Vendedor',
        related_name='notificated_seller',
        on_delete=models.PROTECT)
    amount = models.DecimalField(
        verbose_name="Valor de venda",
        decimal_places=2,
        max_digits=12,
        blank=False,
        null=False)
    average_sales = models.DecimalField(
        verbose_name="Média de vendas",
        decimal_places=2,
        max_digits=12,
        blank=False,
        null=False)
    notification_date = models.DateTimeField(
        verbose_name="Data de notificação",
        blank=False,
        null=False)

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ['-seller', '-notification_date']
