# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150905_0428'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipieIngredients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.IntegerField(default=0)),
                ('ingredient', models.ForeignKey(to='website.Ingredient')),
                ('qty_type', models.ForeignKey(to='website.QtyType')),
            ],
        ),
        migrations.RemoveField(
            model_name='recipeingredients',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='recipeingredients',
            name='qty_type',
        ),
        migrations.RemoveField(
            model_name='recipeingredients',
            name='recipe',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='website.Ingredient', through='website.RecipieIngredients'),
        ),
        migrations.DeleteModel(
            name='RecipeIngredients',
        ),
        migrations.AddField(
            model_name='recipieingredients',
            name='recipe',
            field=models.ForeignKey(to='website.Recipe'),
        ),
    ]
