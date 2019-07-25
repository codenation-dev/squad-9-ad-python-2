from django.core import mail
from django.test import TestCase

from rest_framework import status

from comission.models import ComissionPlan
from seller.models import Address, Seller
from vendas.models import Vendas

# Create your tests here.


class CheckComissionAPITest(TestCase):

    def setUp(self):
        self.comission_plan = ComissionPlan(
            lower_percentage=2.5,
            upper_percentage=10.5,
            min_value=5000.0)
        self.comission_plan.save()

        self.seller_address = Address(
            pk=None,
            street="Rua abcd",
            number="123",
            city="Brasília",
            state="DF",
            country="BR")
        self.seller_address.save()

        self.seller = Seller(
            cpf="12345678910",
            name="José",
            last_name="Vendedor",
            age=30,
            email="sq9p2codenation@gmail.com",
            phone="48012345678",
            address=self.seller_address,
            comission_plan=self.comission_plan)
        self.seller.save()

        Vendas(month=1, seller=self.seller, amount=1000.0).save()
        Vendas(month=2, seller=self.seller, amount=500.0).save()
        Vendas(month=3, seller=self.seller, amount=1100.0).save()

    def test_check_comission_without_notification(self):
        current_sales = {
            'seller': self.seller.id,
            'amount': 970.0,
        }
        response = self.client.post('/check_commision/', current_sales)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Parses response body and check data.
        body = response.json()
        self.assertFalse(body['should_notify'])
        self.assertEqual(len(mail.outbox), 0)

    def test_check_comission_with_notification(self):
        current_sales = {
            'seller': self.seller.id,
            'amount': 966.0,
        }
        response = self.client.post('/check_commision/', current_sales)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Parses response body and check data.
        body = response.json()
        self.assertTrue(body['should_notify'])
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ['sq9p2codenation@gmail.com'])

    def test_check_comission_without_notification_more_months(self):
        Vendas(month=4, seller=self.seller, amount=700.0).save()
        Vendas(month=5, seller=self.seller, amount=650.0).save()
        Vendas(month=6, seller=self.seller, amount=800.0).save()

        current_sales = {
            'seller': self.seller.id,
            'amount': 841.0,
        }
        response = self.client.post('/check_commision/', current_sales)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Parses response body and check data.
        body = response.json()
        self.assertFalse(body['should_notify'])
        self.assertEqual(len(mail.outbox), 0)

    def test_check_comission_with_notification_more_months(self):
        Vendas(month=4, seller=self.seller, amount=700.0).save()
        Vendas(month=5, seller=self.seller, amount=650.0).save()
        Vendas(month=6, seller=self.seller, amount=800.0).save()

        current_sales = {
            'seller': self.seller.id,
            'amount': 839.0,
        }
        response = self.client.post('/check_commision/', current_sales)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Parses response body and check data.
        body = response.json()
        self.assertTrue(body['should_notify'])
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ['sq9p2codenation@gmail.com'])
