# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0008_auto_20151015_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='org',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vapp',
            name='Vapp',
            field=models.CharField(max_length=50),
        ),
    ]
