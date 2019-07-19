from django.test import TestCase

# Create your tests here.
class SellerAPITest(TestCase):

    def test_create_seller(self):
        seller = {
            'cpf': '12345679855',
            'name': 'Joao',
            'last_name': 'da Silva',
            'age': 27,
            'email': 'jpmonteiro64@gmail.com', 
            'phone': '81989429086', 
            'adress': {
                'street': 'Rua Doutor Newton Braga',
                'number': '38',
                'complement': 'Casa 02',
                'city': 'Olinda', 
                'state': 'Pernambuco', 
                'country': 'Brasil'
            }, 
            'comission': 1
        }
        response = self.client.post('/sellers/', seller)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Parses response body and check data.
        body = response.json()
        self.assertTrue(type(body['id'])  == int)
