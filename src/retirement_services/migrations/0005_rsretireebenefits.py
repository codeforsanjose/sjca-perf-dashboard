# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retirement_services', '0004_auto_20151210_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSRetireeBenefits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=0)),
                ('formattedYear', models.CharField(default=None, max_length=40, null=True, blank=True)),
                ('category', models.CharField(max_length=50)),
                ('value', models.FloatField(default=None, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['year'],
                'verbose_name_plural': 'Retirement Services - Retiree Benefits',
            },
        ),
    ]
