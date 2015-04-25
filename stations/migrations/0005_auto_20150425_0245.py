# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0004_auto_20150330_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='wateringstation',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wateringstation',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wateringstation',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
