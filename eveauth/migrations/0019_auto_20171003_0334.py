# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0018_auto_20171002_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='forum_password',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='forum_username',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
