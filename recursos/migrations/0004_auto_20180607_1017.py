# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0003_auto_20180604_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='nombre_recurso',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='referencia',
            field=models.CharField(max_length=100),
        ),
    ]