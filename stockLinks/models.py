# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=10)
    nameinfo = models.CharField(max_length=1000)
    feature = models.CharField(max_length=1000)
    livemethod = models.CharField(max_length=1000)
    feednn = models.CharField(max_length=1000)
    feedmethod = models.CharField(max_length=1000)
