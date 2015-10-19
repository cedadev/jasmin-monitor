# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0003_metric_vapp_vm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vm_core',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('n_cores', models.CharField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Vapp', models.ForeignKey(to='monitoring_system.Vapp')),
            ],
        ),
        migrations.CreateModel(
            name='Vm_ram',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('n_ram', models.CharField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Vapp', models.ForeignKey(to='monitoring_system.Vapp')),
            ],
        ),
        migrations.RemoveField(
            model_name='vm',
            name='Vapp',
        ),
        migrations.DeleteModel(
            name='Vm',
        ),
    ]
