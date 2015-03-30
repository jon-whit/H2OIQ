# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0003_auto_20150320_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wateringstation',
            name='station_id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
