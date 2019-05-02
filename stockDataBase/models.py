from django.db import models

# Create your models here.


class Stock_Basic_Trade_Cal(models.Model):
    exchange = models.CharField(max_length=5)
    cal_date = models.CharField(max_length=10)
    is_open = models.CharField(max_length=2)
    pretrade_date = models.CharField(max_length=10)

