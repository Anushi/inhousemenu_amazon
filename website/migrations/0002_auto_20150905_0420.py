# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='qty_type',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='qty_volume',
        ),
    ]
