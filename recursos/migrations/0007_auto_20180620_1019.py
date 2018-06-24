# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0006_auto_20180614_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='Numero_Serie',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='Estado_Recurso',
            field=models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('EN MANTENIMIENTO', 'EN MANTENIMIENTO'), ('DADO DE BAJA POR PERDIDA', 'DADO DE BAJA POR PERDIDA'), ('DADO DE BAJA POR DA\xd1O TOTAL', 'DADO DE BAJA POR DA\xd1O TOTAL')], default='ACTIVO', max_length=20),
        ),
    ]
