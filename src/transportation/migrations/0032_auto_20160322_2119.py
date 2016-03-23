# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0031_auto_20160322_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authposition',
            name='value',
            field=models.FloatField(default=0),
        ),
    ]
