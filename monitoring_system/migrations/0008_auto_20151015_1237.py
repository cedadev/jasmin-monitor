# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0007_auto_20151015_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='org',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vapp',
            name='Vapp',
            field=models.CharField(max_length=100),
        ),
    ]
