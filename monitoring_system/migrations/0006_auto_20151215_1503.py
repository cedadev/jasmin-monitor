# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_system', '0005_collection_resource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='collection',
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
    ]
