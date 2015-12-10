# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0028_pothole'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoadFunding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=0, verbose_name=b'order')),
                ('formattedYear', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=50)),
                ('value', models.FloatField(default=None, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['year', 'value'],
                'verbose_name_plural': 'Department of Transportation - Funding needed to fix roads',
            },
        ),
    ]
