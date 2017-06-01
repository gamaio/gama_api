# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from  django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField


class api_owners(models.Model):
	# Users who are allowed to have an API app
	user = models.ForeignKey(User, unique=True, blank=False)


class api_apps(models.Model):
	# An Application registered with our API
	owner = models.ForeignKey('api_owners', blank=False)
	apikey = models.CharField(max_length=256, unique=True, blank=False)
	name = models.CharField(max_length=512, unique=True, blank=False)
	description = models.CharField(max_length=2048)
	website = models.URLField(max_length=3000)
	callback_uri = models.URLField(max_length=3000)
	settings = JSONField()


class api_heartbeat(models.Model):
	# If callback_uri is configured and heartbeat is enabled in settings,
	# this can be used to 'ping' the application, as well as communicate
	# changes right away (bypass sync operation and change setting directly, etc)

	api = models.ForeignKey('api_apps', blank=False)
	enabled = models.BooleanField(blank=False)
	time_sent = models.DateTimeField(blank=False)
	time_rcvd = models.DateTimeField(blank=False)
	latency = models.FloatField(blank=False)
	data = JSONField()
