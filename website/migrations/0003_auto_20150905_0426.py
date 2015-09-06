# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150905_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='featured_image',
            field=models.ForeignKey(to='website.Image', blank=True),
        ),
    ]
