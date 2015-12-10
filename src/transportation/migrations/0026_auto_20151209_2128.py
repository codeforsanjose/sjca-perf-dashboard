# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0025_pavementindex'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PavementIndex',
            new_name='PavementIndexArea',
        ),
    ]
