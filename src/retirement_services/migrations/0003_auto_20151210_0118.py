# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retirement_services', '0002_rsauthposition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsauthposition',
            name='formattedYear',
            field=models.CharField(default=b'', max_length=40, null=True, blank=True),
        ),
    ]
