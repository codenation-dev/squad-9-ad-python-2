from django.db import models
from seller.models import Seller


class Sales(models.Model):
    """
        Modelo que representa a venda mensal do vendedor
    """
    months = ((1, "Janeiro"),
              (2, "Fevereiro"),
              (3, "Março"),
              (4, "Abril"),
              (5, "Maio"),
              (6, "Junho"),
              (7, "Julho"),
              (8, "Agosto"),
              (9, "Setembro"),
              (10, "Outubro"),
              (11, "Novembro"),
              (12, "Dezembro"))

    seller = models.ForeignKey(Seller,
                               related_name='seller',
                               on_delete=models.PROTECT,
                               verbose_name='Vendedor')

    month = models.CharField(verbose_name="Mes",
                             choices=months,
                             null=False,
                             blank=False,
                             max_length=15)

    amount = models.DecimalField(verbose_name="Valor",
                                 decimal_places=2,
                                 max_digits=12,
                                 blank=False,
                                 null=False)

    comission = models.DecimalField(verbose_name="Comissao",
                                    decimal_places=2,
                                    max_digits=12,
                                    blank=False,
                                    null=False)

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
        ordering = ['-amount', ]
