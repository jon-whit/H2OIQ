# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wateringstation',
            name='station_id',
            field=models.IntegerField(primary_key=True, unique=True, serialize=False),
        ),
    ]
