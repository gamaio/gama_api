# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170602_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api_owners',
            name='date_deactivated',
            field=models.DateField(blank=True),
        ),
    ]