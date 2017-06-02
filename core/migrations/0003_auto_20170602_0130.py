# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 01:30
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170601_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='api_owners',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='api_owners',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2017, 6, 2, 1, 30, 16, 108889)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='api_owners',
            name='date_deactivated',
            field=models.DateField(default=datetime.datetime(2017, 6, 2, 1, 30, 27, 190835)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='api_owners',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
