# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0016_auto_20151209_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingcitation',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
