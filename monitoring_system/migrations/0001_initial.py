# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('collection_time', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'ordering': ['collection_time'],
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('org_id', models.CharField(max_length=50)),
                ('vm_id', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('metric_type', models.CharField(max_length=3, choices=[('CPU', 'CPU Cores'), ('RAM', 'RAM Used')])),
                ('collection', models.ForeignKey(to='monitoring_system.Collection')),
            ],
        ),
    ]
