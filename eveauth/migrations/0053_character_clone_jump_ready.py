# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-11 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0052_add_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='clone_jump_ready',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]