# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20150905_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='serves',
            field=models.IntegerField(default=1),
        ),
    ]
