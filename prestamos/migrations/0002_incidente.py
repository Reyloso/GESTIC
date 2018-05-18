# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-18 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0002_auto_20180517_2157'),
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('Id_Incidente', models.AutoField(primary_key=True, serialize=False)),
                ('Fecha_Incidente', models.DateField(default=django.utils.timezone.now)),
                ('descripcion', models.TextField(null=True)),
                ('Estado', models.CharField(choices=[('EN REVISION', 'EN REVISION'), ('ACEPTADO', 'ACEPTADO'), ('DADO DE BAJA', 'DADO DE BAJA')], max_length=30)),
                ('Prestamo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prestamos.Prestamo')),
                ('Recurso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recursos.Recurso')),
            ],
            options={
                'verbose_name_plural': 'Registo De Incidentes',
            },
        ),
    ]