# Generated by Django 2.2.7 on 2019-11-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('dbfId', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('playerClass', models.CharField(max_length=200)),
            ],
        ),
    ]
