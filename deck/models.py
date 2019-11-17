from django.db import models

class Card(models.Model):
    """
    For now, only store required fields. 
    Assumption: the field 'name' is used to differentiate whether
    cards are the same, since there are no null values for the 
    column 'name'
    """
    dbfid = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    playerclass = models.CharField(max_length=200)
    