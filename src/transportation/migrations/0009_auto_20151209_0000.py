# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0008_auto_20151208_2353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opexpenditure',
            options={'ordering': ['year', 'value'], 'verbose_name_plural': 'Department of Transportation - Operating Expenditures'},
        ),
    ]
