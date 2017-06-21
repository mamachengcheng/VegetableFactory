from __future__ import unicode_literals

from django.db import models

# Create your models here.


class MinuteStatistics(models.Model):
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    illumination = models.IntegerField(default=0)
    capnography = models.IntegerField(default=0)
    updateTime = models.DateTimeField(auto_now_add=True)


class HourStatistics(models.Model):
    temperature = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    illumination = models.IntegerField(default=0)
    capnography = models.IntegerField(default=0)
    data = models.DateField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now_add=True)


class SittingHistory(models.Model):
    userName = models.CharField(max_length=16, default="root")
    deviceName = models.CharField(max_length=30)
    sittingContent = models.CharField(max_length=16, default="")
    updateTime = models.DateTimeField(auto_now_add=True)
