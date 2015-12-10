# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retirement_services', '0003_auto_20151210_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsauthposition',
            name='formattedYear',
            field=models.CharField(default=None, max_length=40, null=True, blank=True),
        ),
    ]
