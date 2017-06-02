# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class api_owners(models.Model):
	# Users who are allowed to have an API app
	user = models.OneToOneField(User, unique=True, blank=False)
	date_added = models.DateField(blank=False)
	date_deactivated = models.DateField()
	active = models.BooleanField(blank=False)

	def __str__(self):
		return '%s (%s)' % (self.user.username, self.user.id)


@python_2_unicode_compatible
class api_apps(models.Model):
	# An Application registered with our API
	owner = models.ForeignKey('api_owners', blank=False)
	apikey = models.CharField(max_length=256, unique=True, blank=False)
	name = models.CharField(max_length=512, unique=True, blank=False)
	description = models.CharField(max_length=2048)
	website = models.URLField(max_length=3000)
	callback_uri = models.URLField(max_length=3000)
	settings = JSONField()

	def __str__(self):
		return '%s (%s) - %s' % (self.name, self.owner.name, self.apikey)


@python_2_unicode_compatible
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

	def __str__(self):
		return '%s (%s ms)' % (self.api.name, self.latency)
