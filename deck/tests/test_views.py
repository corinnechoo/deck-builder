from django.test import TestCase
from ddt import ddt, data
from django.contrib.auth.models import User

import json


@ddt
class SimpleTest(TestCase):
    """
    Tests that the /cards/ endpoint returns the correct response
    """

    # loads test data into the database
    fixtures = ['test_data.json']

    def setUp(self):
        """
        Logs in with a user
        """
        User.objects.create_superuser(
            'user1',
            'user1@example.com',
            'pswd',
        )
        self.client.login(username="user1", password="pswd")

    def tearDown(self):
        self.client.logout()

    def format_input(self, playerClass):
        """
        Formats the request body for the post request used by all test methods
        """
        return {
            "playerClass": playerClass
        }

    @data('', 123, 'Magician', None)
    def test_details_invalid_input(self, value):
        """
        Tests invalid inputs for the /cards/ endpoint (empty string, integer,
        invalid playerClass, empty value)
        """
        p = self.format_input(value)
        response = self.client.post(
            "/cards/", p, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    @data('Druid', 'Mage')
    def test_details_success(self, value):
        """
        Tests that the endpoint returns at most 30 cards, with fewer than
        2 cards having the same name given the test data containing the
        following playerClass: 27 Neutral, 1 Mage, 4 Druid

        """
        p = self.format_input(value)
        response = self.client.post(
            "/cards/", p, content_type='application/json')
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
