# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0003_auto_20151207_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opexpbyservice',
            name='expenditure',
            field=models.FloatField(),
        ),
    ]
