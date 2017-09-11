# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone
# Create your models here.


class UserInfo(models.Model):
    user_name = models.CharField(max_length=100)
    user_pwd = models.CharField(max_length=32)     # md-5加密最后结果为32位
    user_register_time = models.DateTimeField(default=timezone.now)  # 当前的系统时间
    user_head_img = models.CharField(max_length=255)
    user_login_time = models.DateTimeField(default=timezone.now)   # 每次登录的系统时间
    user_email = models.EmailField(null=True)   # 可以为空



