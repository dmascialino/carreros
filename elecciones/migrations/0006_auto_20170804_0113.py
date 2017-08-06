# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0005_auto_20170804_0103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eleccion',
            options={'verbose_name': 'Elección', 'verbose_name_plural': 'Elecciones'},
        ),
        migrations.AlterModelOptions(
            name='opcion',
            options={'verbose_name': 'Opción', 'verbose_name_plural': 'Opciones'},
        ),
        migrations.AddField(
            model_name='partido',
            name='numero',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
