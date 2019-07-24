from django.db import models


class ComissionPlan(models.Model):
    """
        Model that represents systems' comission plans
    """

    lower_percentage = models.DecimalField(
        verbose_name="Porcentagem Menor",
        decimal_places=2,
        max_digits=5,
        null=False,
        blank=False)
    upper_percentage = models.DecimalField(
        verbose_name="Porcentagem Maior",
        decimal_places=2,
        max_digits=5,
        null=False,
        blank=False)
    min_value = models.DecimalField(
        verbose_name="Valor Minimo",
        decimal_places=2,
        max_digits=12,
        blank=False,
        null=False)

    def __str__(self):
        return f"""
            {self.id}.
             Porcentagem Menor: {self.lower_percentage}%\
             - se vender o Valor Mínimo de R${self.min_value}\
             recebe a Porcentagem Maior: {self.upper_percentage}%
        """

    class Meta:
        verbose_name = "Comissão"
        verbose_name_plural = "Comissões"
        ordering = ['upper_percentage', 'lower_percentage', 'min_value']
