# **coding: utf-8**
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class DeviceControl(models.Model):

    CONTROL_STATUE_CHOICE = (
        (0, "关闭"),
        (1, "开起"),
        (3, "调节"),
    )

    CONTROL_TYPE_CHOICE = (
        (0, "开关控制"),
        (1, "强度控制"),
    )

    control_num = models.IntegerField("控制代号")
    control_statue = models.IntegerField("控制状态", default=0, choices=CONTROL_STATUE_CHOICE)
    control_type = models.IntegerField("控制类型", choices=CONTROL_TYPE_CHOICE)
    control_name = models.CharField("控制方法名", max_length=30)
    control_code = models.CharField("控制代码", max_length=30)
