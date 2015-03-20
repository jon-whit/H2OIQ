# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_auto_20150320_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wateringstation',
            name='id',
        ),
        migrations.AlterField(
            model_name='wateringstation',
            name='station_id',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
