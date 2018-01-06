# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0041_kill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kill',
            old_name='loser',
            new_name='victim',
        ),
        migrations.AddField(
            model_name='kill',
            name='date',
            field=models.DateTimeField(db_index=True, default=None),
            preserve_default=False,
        ),
    ]