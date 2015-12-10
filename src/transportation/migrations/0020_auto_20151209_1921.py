# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0019_drainrequest_stormcall_streetsweeping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drainrequest',
            name='value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='streetsweeping',
            name='value',
            field=models.FloatField(),
        ),
    ]
