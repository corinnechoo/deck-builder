# Generated by Django 2.2.7 on 2019-11-16 18:19
from django.db import migrations, models
from django.db import transaction
from deckbuilder.settings import HEARTHSTONE_KEY

import requests
import os


def add_card(apps, schema_editor):
    CardDetails = apps.get_model('deck', 'Card')
    headers = {
        'X-Mashape-Key': HEARTHSTONE_KEY
    }
    response = requests.get(
        "https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/Rastakhan%27s%20Rumble", headers=headers)

    if response.status_code != 200:
        pass

    data_list = response.json()

    for data in data_list:
        playerClass = data.get('playerClass')
        dbfId = data.get('dbfId')
        name = data.get('name')

        if None not in (playerClass, dbfId, name):
            card = CardDetails(dbfId, name, playerClass)
            card.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deck', '0001_initial')
    ]

    operations = [
        migrations.RunPython(add_card),
    ]