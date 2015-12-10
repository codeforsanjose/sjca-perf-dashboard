# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0029_roadfunding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadfunding',
            name='formattedYear',
            field=models.CharField(default=None, max_length=40, null=True, blank=True),
        ),
    ]
