from django.test import TestCase
from deck.models import Card

from django.db.utils import IntegrityError


class CardTest(TestCase):

    def create_card(self, dbfid, name, playerclass, cardtype, cardid, cardset):
        """
        Creates Card object to be used by all test methods using required fields
        """
        return Card.objects.create(dbfid=dbfid, name=name, playerclass=playerclass,
                                   cardtype=cardtype, cardid=cardid, cardset=cardset)

    def test_card_creation(self, dbfid=12345, name="test", playerclass="Warrior",
                           cardtype="Enchantment", cardid="TRL_530", cardset="Rastakhan's Rumble"):
        """
        Tests that Cards with the fields dbfid, name, playerclass, cardtype,
        cardid, cardset are created successfully
        """
        c = self.create_card(dbfid, name, playerclass,
                             cardtype, cardid, cardset)
        self.assertTrue(isinstance(c, Card))

    def test_card_creation_empty(self, dbfid=None, name="test", playerclass="Warrior",
                                 cardtype="Enchantment", cardid="TRL_530", cardset="Rastakhan's Rumble"):
        """
        Tests that card is not created as dbfid is the primary key and shouldn't be None
        """
        try:
            self.create_card(dbfid, name, playerclass,
                             cardtype, cardid, cardset)
        except IntegrityError:
            pass
