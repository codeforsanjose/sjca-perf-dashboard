# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0012_auto_20151209_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignalActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=0)),
                ('formattedYear', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=50)),
                ('value', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['year', 'value'],
                'verbose_name_plural': 'Department of Transportation - Signal Activities',
            },
        ),
    ]
