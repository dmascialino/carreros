# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prensa', '0003_programa_fuente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ('apellido',)},
        ),
        migrations.AlterField(
            model_name='programa',
            name='medio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programas', to='prensa.Medio'),
        ),
    ]
