# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vapp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Vapp', models.CharField(max_length=30)),
                ('metric', models.ForeignKey(to='monitoring_system.Metric')),
            ],
        ),
        migrations.CreateModel(
            name='Vm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('n_cores', models.CharField(max_length=2)),
                ('Vapp', models.ForeignKey(to='monitoring_system.Vapp')),
            ],
        ),
    ]
