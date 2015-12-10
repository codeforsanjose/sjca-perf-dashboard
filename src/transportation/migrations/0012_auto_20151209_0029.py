# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0011_auto_20151209_0028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modeofcommute',
            options={'ordering': ['year', 'value'], 'verbose_name_plural': 'Department of Transportation - Mode of Commute'},
        ),
    ]
