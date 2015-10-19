# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0005_auto_20151015_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vm_ram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_ram', models.CharField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Vapp', models.ForeignKey(to='monitoring_system.Vapp')),
            ],
        ),
    ]
