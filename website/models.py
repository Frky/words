from __future__ import unicode_literals

from django.db import models

from website.random_primary import RandomPrimaryIdModel

class Word(models.Model):
    word = models.CharField(max_length=255, blank=False, null=False)
    bg_color = models.CharField(max_length=7, default="#ffffff")
    fg_color = models.CharField(max_length=7, default="#000000")
    top = models.IntegerField()
    left = models.IntegerField()
    zindex = models.IntegerField()
    size = models.FloatField()

