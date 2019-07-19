# coding=utf-8
from django.db import models
from comission.models import ComissionPlan


class Address(models.Model):
    """
        Modelo que representa o endereço do vendedor
    """

    street = models.CharField(verbose_name="Logradouro", null=False, blank=False, max_length=150)
    number = models.CharField(verbose_name="Numero", null=False, blank=True, max_length=10)
    complement = models.CharField(verbose_name="Complemento", null=True, blank=True, max_length=150)
    city = models.CharField(verbose_name="Cidade", max_length=150)
    state = models.CharField(verbose_name="Estado", max_length=150)
    country = models.CharField(verbose_name="País", null=False, blank=False, max_length=150, default="Brasil")

    def __str__(self):
        return self.street + self.number + self.complement if self.complement != None else self.street + self.number

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endreços"
        ordering = ['city', 'state']


class Seller(models.Model):
    """
        Modelo que representa o vendedor
    """

    cpf = models.CharField(verbose_name="CPF", null=False, blank=False, max_length=11, unique=True)
    name = models.CharField(verbose_name="Nome", null=False, blank=False, max_length=30)
    last_name = models.CharField(verbose_name="Sobrenome", null=False, blank=False, max_length=30)
    age = models.IntegerField(verbose_name="Idade", null=False, blank=False)
    email = models.EmailField(verbose_name="Email", max_length=80, blank=False, null=False)
    phone = models.CharField(verbose_name="Telefone", max_length=11, blank=False, null=False)
    address = models.OneToOneField(Address, related_name='address', on_delete=models.CASCADE,
                                    verbose_name='Endereco')
    comission = models.ForeignKey(ComissionPlan, related_name='comission', on_delete=models.CASCADE,
                                    verbose_name='Comissao')

    def __str__(self):
        return self.name + self.last_name

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        ordering = ['name', 'age']