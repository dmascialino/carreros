# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiscales', '0005_fiscal_barrio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='referentes',
            field=models.ManyToManyField(help_text='referentes_de_la_orga', related_name='es_referente_de', to='fiscales.Fiscal'),
        ),
    ]
