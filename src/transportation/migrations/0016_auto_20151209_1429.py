# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0015_parkingcitation_parkingdowntown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingcitation',
            name='value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='parkingdowntown',
            name='value',
            field=models.FloatField(),
        ),
    ]
