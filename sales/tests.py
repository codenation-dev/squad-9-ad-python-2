from django.test import TestCase

from rest_framework import status

from comission.models import ComissionPlan
from seller.models import Address, Seller


class SalesAPITest(TestCase):

    def setUp(self):
        self.comission_plan = ComissionPlan(
            lower_percentage=5,
            upper_percentage=10,
            min_value=2000.0)
        self.comission_plan.save()

        self.seller_address = Address(
            pk=None,
            street="Rua tal",
            number="10",
            city="sao paulo",
            state="SP",
            country="Brasil")
        self.seller_address.save()

        self.seller = Seller(
            cpf="12345612396",
            name="Rob",
            last_name="Vendedor",
            age=29,
            email="bobcoutinho@gmail.com",
            phone="11970750623",
            address=self.seller_address,
            comission_plan=self.comission_plan)
        self.seller.save()

    def test_submit_month_comission_low(self):
        sale = {
            'amount': 1000,
            'seller': self.seller.id,
            'comission': self.seller.comission_plan.id,
            'month': 1,
            'year': 2018
        }
        response = self.client.post('/month_comission/', sale)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Parses response body and check data.
        body = response.json()
        self.assertEqual(body['id'], 1)
        self.assertEqual(body['comission'], 50)

    def test_submit_month_comission_up(self):
        sale = {
            'amount': 2000,
            'seller': self.seller.id,
            'comission': self.seller.comission_plan.id,
            'month': 1,
            'year': 2018
        }
        response = self.client.post('/month_comission/', sale)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Parses response body and check data.
        body = response.json()
        self.assertEqual(body['id'], 1)
        self.assertEqual(body['comission'], 200)

    def test_submit_month_comission_invalid_year(self):
        sale = {
            'amount': 2000,
            'seller': self.seller.id,
            'comission': self.seller.comission_plan.id,
            'month': 1,
            'year': 2020
        }
        response = self.client.post('/month_comission/', sale)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
