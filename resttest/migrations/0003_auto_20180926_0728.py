# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-26 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resttest', '0002_auto_20180926_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='departure_date',
            field=models.DateField(help_text='\ucd9c\ubc1c\ub0a0\uc9dc', null=True, verbose_name='\ucd9c\ubc1c\ub0a0\uc9dc'),
        ),
    ]
