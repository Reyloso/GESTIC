# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0007_auto_20180620_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='Numero_Serie',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
