from rest_framework.test import APITestCase
from rest_framework import status
from comission.models import ComissionPlan
from sales.models import Sales
from seller import models


# Create your tests here.
class SellerAPITest(APITestCase):
    def setUp(self):
        self.comission_plan = ComissionPlan(
            lower_percentage=2.5,
            upper_percentage=10.5,
            min_value=5000.0)
        self.comission_plan.save()

        self.seller_address = models.Address(
            pk=None,
            street="Rua abcd",
            number="123",
            city="Brasília",
            state="DF",
            country="BR")
        self.seller_address.save()

        self.seller = models.Seller(
            cpf="12345678910",
            name="José",
            last_name="Vendedor",
            age=30,
            email="sq9p2codenation@gmail.com",
            phone="48012345678",
            address=self.seller_address,
            comission_plan=self.comission_plan)
        self.seller.save()

        self.seller2_address = models.Address(
            pk=None,
            street="Rua abcd",
            number="123",
            city="Brasília",
            state="DF",
            country="BR")
        self.seller2_address.save()

        self.seller2 = models.Seller(
            cpf="12345612396",
            name="Joao",
            last_name="Vendedor",
            age=27,
            email="jpmonteiro64@gmail.com",
            phone="48012345678",
            address=self.seller2_address,
            comission_plan=self.comission_plan)
        self.seller2.save()

        self.seller3_address = models.Address(
            pk=None,
            street="Rua abcd",
            number="123",
            city="Brasília",
            state="DF",
            country="BR")
        self.seller3_address.save()

        self.seller3 = models.Seller(
            cpf="74185296346",
            name="Luis",
            last_name="Vendedor",
            age=27,
            email="luis@gmail.com",
            phone="48012345678",
            address=self.seller3_address,
            comission_plan=self.comission_plan)
        self.seller3.save()

        Sales(month=1, seller=self.seller, amount=1000.0, comission=25).save()
        Sales(month=2, seller=self.seller, amount=500.0, comission=12).save()
        Sales(month=3, seller=self.seller, amount=1100.0, comission=27).save()
        Sales(month=1, seller=self.seller2, amount=500.0, comission=12).save()
        Sales(month=2, seller=self.seller2, amount=1100.0, comission=27).save()
        Sales(month=3, seller=self.seller2, amount=1000.0, comission=25).save()
        Sales(month=1, seller=self.seller3, amount=1100.0, comission=27).save()
        Sales(month=2, seller=self.seller3, amount=1000.0, comission=25).save()
        Sales(month=3, seller=self.seller3, amount=500.0, comission=12).save()

    def test_create_seller(self):
        comission_plan = {
            'lower_percentage': 2.5,
            'min_value': 15000.00,
            'upper_percentage': 15.0
        }
        response = self.client.post('/comissions/',
                                    comission_plan, format='json')

        seller = {
            'cpf': '12345679855',
            'name': 'Joao',
            'last_name': 'da Silva',
            'age': 27,
            'email': 'jpmonteiro64@gmail.com',
            'phone': '81989429086',
            'address': {
                'street': 'Rua Doutor Newton Braga',
                'number': '38',
                'complement': 'Casa 02',
                'city': 'Olinda',
                'state': 'Pernambuco',
                'country': 'Brasil'
            },
            'comission_plan': 1
        }
        response = self.client.post('/sellers/', seller, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Parses response body and check data.
        body = response.json()
        self.assertTrue(type(body['id']) == int)

    def test_retrieve_sellers_month(self):
        response = self.client.get('/best_sellers/0/2')
        body = response.json()
        print(body)
