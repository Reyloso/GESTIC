# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0004_auto_20180607_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca', models.CharField(max_length=60, null=True)),
            ],
            options={
                'verbose_name_plural': 'Marca',
            },
        ),
        migrations.AddField(
            model_name='recurso',
            name='Marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recursos.Marca'),
        ),
    ]