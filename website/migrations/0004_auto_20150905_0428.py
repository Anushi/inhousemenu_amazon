# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20150905_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='featured_image',
            field=models.ForeignKey(to='website.Image', null=True),
        ),
    ]
