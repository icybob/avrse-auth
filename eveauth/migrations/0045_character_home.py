# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-06 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sde', '0019_auto_20171231_0418'),
        ('eveauth', '0044_auto_20180106_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='home',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='sde.Station'),
        ),
    ]
