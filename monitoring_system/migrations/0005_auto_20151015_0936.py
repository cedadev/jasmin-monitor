# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0004_auto_20151015_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vm_ram',
            name='Vapp',
        ),
        migrations.DeleteModel(
            name='Vm_ram',
        ),
    ]
