# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 09:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anticounterfeit', '0011_auto_20151207_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='stateFK',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='cityFK',
        ),
    ]
