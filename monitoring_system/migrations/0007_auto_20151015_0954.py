# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0006_vm_ram'),
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
