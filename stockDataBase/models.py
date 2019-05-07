from django.db import models

# Create your models here.


class Stock_Basic_Trade_Cal(models.Model):
    exchange = models.CharField(max_length=5)
    cal_date = models.CharField(max_length=10)
    is_open = models.CharField(max_length=2)
    pretrade_date = models.CharField(max_length=10)


class Stock_Basic_User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    truename = models.CharField(max_length=30)
    email = models.CharField(max_length=36)
    authority = models.CharField(max_length=8)
    deleted = models.CharField(max_length=5)
