
# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-11 05:38
from __future__ import unicode_literals

from django.db import migrations


def add_groups(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0051_structure_fuel_expires'),
    ]

    operations = [
        migrations.RunPython(add_groups),
    ]
