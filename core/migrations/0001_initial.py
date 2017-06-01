# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 07:08
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='api_apps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apikey', models.CharField(max_length=256, unique=True)),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.CharField(max_length=2048)),
                ('website', models.URLField(max_length=3000)),
                ('callback_uri', models.URLField(max_length=3000)),
                ('settings', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='api_heartbeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField()),
                ('time_sent', models.DateTimeField()),
                ('time_rcvd', models.DateTimeField()),
                ('latency', models.FloatField()),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('api_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.api_apps')),
            ],
        ),
        migrations.CreateModel(
            name='api_owners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='api_apps',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.api_owners'),
        ),
    ]
