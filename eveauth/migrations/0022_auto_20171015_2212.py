# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 22:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0021_groupdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupdetails',
            old_name='is_discord',
            new_name='discord',
        ),
        migrations.RenameField(
            model_name='groupdetails',
            old_name='is_forum',
            new_name='forum',
        ),
        migrations.RenameField(
            model_name='groupdetails',
            old_name='is_mumble',
            new_name='mumble',
        ),
    ]
