# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0002_auto_20151015_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('org', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vapp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Vapp', models.CharField(max_length=30)),
                ('metric', models.ForeignKey(to='monitoring_system.Metric')),
            ],
        ),
        migrations.CreateModel(
            name='Vm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('n_cores', models.CharField(max_length=2)),
                ('Vapp', models.ForeignKey(to='monitoring_system.Vapp')),
            ],
        ),
    ]
