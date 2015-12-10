# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0020_auto_20151209_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drainrequest',
            name='value',
            field=models.FloatField(default=None),
        ),
    ]
