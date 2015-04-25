# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WateringStation',
            fields=[
                ('station_id', models.BigIntegerField(serialize=False, unique=True, primary_key=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
