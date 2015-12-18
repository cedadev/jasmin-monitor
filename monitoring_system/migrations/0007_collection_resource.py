# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0006_auto_20151215_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('collection_time', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'ordering': ['collection_time'],
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('org_name', models.CharField(max_length=50)),
                ('vm_id', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('metric_type', models.CharField(choices=[('CPU', 'CPU Cores'), ('RAM', 'RAM Used')], max_length=3)),
                ('collection', models.ForeignKey(to='monitoring_system.Collection')),
            ],
        ),
    ]
