from __future__ import unicode_literals

from django.db import models


class Summoner(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
