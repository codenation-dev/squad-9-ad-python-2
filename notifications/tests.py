from datetime import datetime

from django.core import mail

from rest_framework import status
from rest_framework.test import APITransactionTestCase

from comission.models import ComissionPlan
from notifications.models import Notification
from sales.models import Sales
from seller.models import Address, Seller

# Create your tests here.


class NotificationsAPITest(APITransactionTestCase):

    def setUp(self):
        self.seller = _set_up_seller()

        self.first_notification = Notification(
            seller=self.seller,
            amount=965.0,
            average_sales=966.67,
            notification_date=datetime.now())
        self.first_notification.save()

        self.second_notification = Notification(
            seller=self.seller,
            amount=1000.0,
            average_sales=1010.0,
            notification_date=datetime.now())
        self.second_notification.save()

    def test_list_notifications(self):
        response = self.client.get('/notifications/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Parses response body and check data.
        body = response.json()
        self.assertEqual(len(body), 2)

        sorted_amounts = sorted([float(n['amount']) for n in body])
        self.assertEqual(sorted_amounts, [965.0, 1000.0])

    def test_get_notification(self):
        # First notification request
        url = f'/notifications/{self.first_notification.id}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        body = response.json()
        self.assertEqual(body['amount'], '965.00')

        # Second notification request
        url = f'/notifications/{self.second_notification.id}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        body = response.json()
        self.assertEqual(body['amount'], '1000.00')


class CheckComissionAPITest(APITransactionTestCase):

    def setUp(self):
        self.seller = _set_up_seller()

        Sales(month=1, seller=self.seller, amount=1000.0, comission=25).save()
        Sales(month=2, seller=self.seller, amount=500.0, comission=12.5).save()
        Sales(month=3, seller=self.seller, amount=1100.0, comission=27).save()

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
        Sales(month=4, seller=self.seller, amount=700.0, comission=17.5).save()
        Sales(month=5, seller=self.seller, amount=650.0, comission=16.2).save()
        Sales(month=6, seller=self.seller, amount=800.0, comission=20).save()

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
        Sales(month=4, seller=self.seller, amount=700.0, comission=17.5).save()
        Sales(month=5, seller=self.seller, amount=650.0, comission=16.2).save()
        Sales(month=6, seller=self.seller, amount=800.0, comission=20).save()

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


def _set_up_seller():
    comission_plan = ComissionPlan(
        lower_percentage=2.5,
        upper_percentage=10.5,
        min_value=5000.0)
    comission_plan.save()

    seller_address = Address(
        pk=None,
        street="Rua abcd",
        number="123",
        city="Brasília",
        state="DF",
        country="BR")
    seller_address.save()

    seller = Seller(
        cpf="12345678910",
        name="José",
        last_name="Vendedor",
        age=30,
        email="sq9p2codenation@gmail.com",
        phone="48012345678",
        address=seller_address,
        comission_plan=comission_plan)
    seller.save()

    return seller
