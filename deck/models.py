from django.db import models
from jsonfield import JSONField


class Card(models.Model):
    """
    Defines the card model. It is assumed that all cards must have a dbfId,
    name, playerClass, cardId, cardSet and cardType, and the dbfId is always
    unique so it is used as the primary key.
    """
    dbfid = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(db_index=True, max_length=200)
    playerclass = models.CharField(db_index=True, max_length=200)
    armor = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=200, blank=True, null=True)
    attack = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    cardid = models.CharField(max_length=200)
    cardset = models.CharField(max_length=200)
    collectible = models.BooleanField(max_length=200, blank=True, null=True)
    cost = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    durability = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True)
    elite = models.BooleanField(max_length=200, blank=True, null=True)
    faction = models.CharField(max_length=200, blank=True, null=True)
    flavor = models.CharField(max_length=200, blank=True, null=True)
    health = models.CharField(max_length=200, blank=True, null=True)
    img = models.CharField(max_length=200, blank=True, null=True)
    imggold = models.CharField(max_length=200, blank=True, null=True)
    locale = models.CharField(max_length=200, blank=True, null=True)
    mechanics = JSONField(blank=True, null=True)
    race = models.CharField(max_length=200, blank=True, null=True)
    rarity = models.CharField(max_length=200, blank=True, null=True)
    cardtype = models.CharField(max_length=200)
