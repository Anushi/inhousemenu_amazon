# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20150905_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipieingredients',
            name='volume',
            field=models.FloatField(default=0),
        ),
    ]
