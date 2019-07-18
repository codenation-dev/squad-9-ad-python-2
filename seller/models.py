# coding=utf-8
from django.db import models
from comission.models import ComissionPlan


class Endereco(models.Model):
    """
        Modelo que representa o endereço do vendedor
    """

    logradouro = models.CharField(verbose_name="Logradouro", null=False, blank=False, max_length=150)
    numero = models.CharField(verbose_name="Numero", null=False, blank=True, max_length=10)
    complemento = models.CharField(verbose_name="Complemento", null=True, blank=True, max_length=150)
    cidade = models.CharField(verbose_name="Cidade", max_length=150)
    estado = models.CharField(verbose_name="Estado", max_length=150)
    pais = models.CharField(verbose_name="País", null=False, blank=False, max_length=150, default="Brasil")

    def __str__(self):
        return self.logradouro + self.numero + self.complemento if self.complemento != None else self.logradouro + self.numero

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endreços"
        ordering = ['cidade', 'estado']


class Vendedor(models.Model):
    """
        Modelo que representa o vendedor
    """

    cpf = models.CharField(verbose_name="CPF", null=False, blank=False, max_length=11, unique=True)
    nome = models.CharField(verbose_name="Nome", null=False, blank=False, max_length=30)
    sobrenome = models.CharField(verbose_name="Sobrenome", null=False, blank=False, max_length=30)
    idade = models.IntegerField(verbose_name="Idade", null=False, blank=False)
    email = models.EmailField(verbose_name="Email", max_length=80, blank=False, null=False)
    endereco = models.OneToOneField(Endereco, related_name='endereco', on_delete=models.CASCADE,
                                    verbose_name='Endereco')
    comissao = models.OneToOneField(ComissionPlan, related_name='comissao', on_delete=models.CASCADE,
                                    verbose_name='Comissao')

    def __str__(self):
        return self.nome + self.sobrenome

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        ordering = ['nome', 'idade']


class Telefone(models.Model):
    """
        Modelo que representa o teleofne do vendedor
    """

    vendedor = models.ForeignKey(Vendedor, related_name='telefone_vendedor', on_delete=models.CASCADE,
                                 verbose_name='Vendedor')
    ddd = models.CharField(verbose_name="DDD", null=False, blank=False, max_length=2)
    numero_telefone = models.CharField(verbose_name="Numero", null=False, blank=False, max_length=15)

    def __str__(self):
        return self.ddd + self.numero_telefone

    class Meta:
        verbose_name = "Telefone"
        verbose_name_plural = "Telefones"
        ordering = ['ddd', 'numero_telefone']


