# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0017_auto_20180620_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidente',
            name='Tipo_Incidente',
            field=models.CharField(choices=[('DA\xd1O PARCIAL DEL RECURSO', 'DA\xd1O PARCIAL DEL RECURSO'), ('DA\xd1O TOTAL DEL RECURSO', 'DA\xd1O TOTAL DEL RECURSO'), ('PERDIDA DEL RECURSO', 'PERDIDA DEL RECURSO'), ('OTRO', 'OTRO')], default='OTRO', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incidente',
            name='Estado',
            field=models.CharField(choices=[('EN REVISION', 'EN REVISION'), ('REVISADO', 'REVISADO')], max_length=30),
        ),
    ]
