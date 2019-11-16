from django.test import TestCase
from deck.models import Card

from django.db.utils import IntegrityError


# models test

class CardTest(TestCase):

    def create_card(self, dbfId, name, playerClass):
        return Card.objects.create(dbfId=dbfId, name=name, playerClass=playerClass)

    def test_card_creation(self, dbfId=12345, name="test", playerClass="Warrior"):
        c = self.create_card(dbfId, name, playerClass)
        self.assertTrue(isinstance(c, Card))

    def test_card_creation_empty(self, dbfId=None, name="test", playerClass="Warrior"):
        try:
            self.create_card(dbfId, name, playerClass)
        except IntegrityError:
            pass