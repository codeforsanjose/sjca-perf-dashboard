# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0002_opexpbyservice_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opexpbyservice',
            name='expenditure',
            field=models.DecimalField(max_digits=10, decimal_places=10),
        ),
    ]
