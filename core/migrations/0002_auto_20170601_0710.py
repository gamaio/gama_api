# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 07:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='api_apps',
            old_name='owner_id',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='api_heartbeat',
            old_name='api_id',
            new_name='api',
        ),
        migrations.RenameField(
            model_name='api_owners',
            old_name='user_id',
            new_name='user',
        ),
    ]
