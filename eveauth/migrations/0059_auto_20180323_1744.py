# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-23 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0058_groupdetails_access_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupdetails',
            name='access_level',
            field=models.IntegerField(choices=[(0, b'Non-Members'), (1, b'Blues'), (2, b'Members')], default=2, verbose_name=b'Minimum Access Level'),
        ),
        migrations.AlterField(
            model_name='groupdetails',
            name='can_apply',
            field=models.BooleanField(default=False, verbose_name=b'Can Apply'),
        ),
        migrations.AlterField(
            model_name='groupdetails',
            name='discord',
            field=models.BooleanField(default=False, verbose_name=b'Send to Discord'),
        ),
        migrations.AlterField(
            model_name='groupdetails',
            name='forum',
            field=models.BooleanField(default=False, verbose_name=b'Send to Forum'),
        ),
        migrations.AlterField(
            model_name='groupdetails',
            name='is_open',
            field=models.BooleanField(default=False, verbose_name=b'Open Group'),
        ),
        migrations.AlterField(
            model_name='groupdetails',
            name='mumble',
            field=models.BooleanField(default=True, verbose_name=b'Send to Mumble'),
        ),
    ]