# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0005_auto_20150425_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wateringstation',
            name='station_id',
            field=models.BigIntegerField(primary_key=True, unique=True, serialize=False),
        ),
    ]
