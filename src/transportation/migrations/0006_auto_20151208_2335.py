# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0005_auto_20151208_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opexpbyservice',
            old_name='expenditure',
            new_name='value',
        ),
    ]
