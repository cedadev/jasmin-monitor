# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vapp',
            name='metric',
        ),
        migrations.RemoveField(
            model_name='vm',
            name='Vapp',
        ),
        migrations.DeleteModel(
            name='Metric',
        ),
        migrations.DeleteModel(
            name='Vapp',
        ),
        migrations.DeleteModel(
            name='Vm',
        ),
    ]
