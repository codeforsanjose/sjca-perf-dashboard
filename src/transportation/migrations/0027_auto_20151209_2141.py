# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0026_auto_20151209_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='PavementIndexSJ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=0)),
                ('formattedYear', models.CharField(max_length=20)),
                ('value', models.FloatField(default=None, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['year', 'value'],
                'verbose_name_plural': 'Department of Transportation - Pavement Index San Jose',
            },
        ),
        migrations.AlterModelOptions(
            name='pavementindexarea',
            options={'ordering': ['year', 'value'], 'verbose_name_plural': 'Department of Transportation - Pavement Index by Area'},
        ),
    ]
