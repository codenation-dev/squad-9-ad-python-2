from django.db import models
from vendedor.models import Vendedor


class Vendas(models.Model):
    """
        Modelo que representa a venda mensal do vendedor
    """
    meses = (('Janeiro', 'Janeiro'), ("Fevereiro", "Fevereiro"), ("Março", "Março"), ("Abril", "Abril"),
             ("Maio", "Maio"), ("Junho", "Junho"), ("Julho", "Julho"), ("Agosto", "Agosto"), ("Setembro", "Setembro"),
             ("Outubro", "Outubro"), ("Novembro", "Novembro"), ("Dezembro", "Dezembro"))

    vendedor = models.ForeignKey(Vendedor, related_name='comissao_vendedor', on_delete=models.CASCADE,
                                 verbose_name='Vendedor')

    mes = models.CharField(verbose_name="Mes", choices=meses, null=False, blank=False, max_length=15)

    valor_venda = models.DecimalField(verbose_name="Valor Minimo", decimal_places=2, max_digits=12, blank=False,
                                       null=False)

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
        ordering = ['-valor_venda', ]
