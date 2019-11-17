from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from ddt import ddt, data

from ..views import index
import json


@ddt
class SimpleTest(TestCase):

    fixtures = ['test_data.json']

    def setUp(self):
        self.factory = RequestFactory()

    def format_input(self, playerClass):
        return {
            "playerClass": playerClass
        }

    @data('', 123, 'Magician')
    def test_details_invalid_input(self, value):
        p = self.format_input(value)
        response = self.client.post("", p, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    @data('Druid', 'Mage')
    # there are 27 neutral cards, 1 mage, 4 druid
    def test_details_success(self, value):
        """  

        
        """
        p = self.format_input(value)
        response = self.client.post("", p, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.content)
        self.assertTrue(len(response_json) <= 30)

        name_store = dict()

        for row in response_json:
            name = row['name']
            if name in name_store:
                name_store[name] += 1
            else:
                name_store[name] = 1
        for _, val in name_store.items():
            self.assertTrue(val <= 2)
