from django.db import models


class Comissao(models.Model):
    """
        Modelo que representa a comissao do vendedor
    """

    nome = models.CharField(verbose_name="Nome Comissao", null=False, blank=False, max_length=30)
    porcentagem_menor = models.DecimalField(verbose_name="Porcentagem Menor", decimal_places=2, max_digits=5,
                                            null=False, blank=False)
    porcentagem_maior = models.DecimalField(verbose_name="Porcentagem Maior", decimal_places=2, max_digits=5,
                                            null=False, blank=False)
    valor_minimo = models.DecimalField(verbose_name="Valor Minimo", decimal_places=2, max_digits=12, blank=False,
                                       null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Comissão"
        verbose_name_plural = "Comissões"
        ordering = ['nome', 'porcentagem_maior', 'porcentagem_menor', 'valor_minimo']
