from django.db import models
from vendedor.models import Vendedor


class Notificacoes(models.Model):
    """
        Modelo que representa as notificacoes do vendedor
    """

    vendedor = models.ForeignKey(Vendedor, related_name='notificacoes_vendedor', on_delete=models.CASCADE,
                                 verbose_name='Vendedor')

    media_venda = models.DecimalField(verbose_name="Média comissão", decimal_places=2, max_digits=12, blank=False,
                                       null=False)

    class Meta:
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"
        ordering = ['-media_venda', ]

