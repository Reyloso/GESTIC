# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0016_auto_20180618_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='Estado_prestamo',
            field=models.CharField(choices=[('EN CURSO', 'EN CURSO'), ('DEVUELTO', 'DEVUELTO')], max_length=20),
        ),
    ]
