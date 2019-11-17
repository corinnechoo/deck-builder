from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from ddt import ddt, data

from ..views import index


@ddt
class SimpleTest(TestCase):

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


