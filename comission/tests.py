from django.test import TestCase

from rest_framework import status

# Create your tests here.


class ComissionPlanAPITest(TestCase):

    def test_create_comission_plan(self):
        comission_plan = {
            'lower_percentage': 2.5,
            'min_value': 15000.00,
            'upper_percentage': 15.0,
        }
        response = self.client.post('/comissions/', comission_plan)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Parses response body and check data.
        body = response.json()
        self.assertEqual(body['id'], 1)
