# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0030_auto_20151210_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opexpenditure',
            name='value',
            field=models.FloatField(default=0),
        ),
    ]
