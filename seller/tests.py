from rest_framework.test import APITestCase
from rest_framework import status


# Create your tests here.
class SellerAPITest(APITestCase):

    def test_create_seller(self):
        comission_plan = {
            'lower_percentage': 2.5,
            'min_value': 15000.00,
            'upper_percentage': 15.0
        }
        response = self.client.post('/comissions/', comission_plan, format='json')

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
