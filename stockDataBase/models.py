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


class Stock_Basic_List(models.Model):
    ts_code = models.CharField(max_length=12)
    symbol = models.CharField(max_length=8)
    name = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    industry = models.CharField(max_length=30)
    fullname = models.CharField(max_length=255)
    enname = models.CharField(max_length=255)
    market = models.CharField(max_length=30)
    exchange = models.CharField(max_length=8)
    curr_type = models.CharField(max_length=30)
    list_status = models.CharField(max_length=8)
    list_date = models.CharField(max_length=12)
    delist_date = models.CharField(max_length=12)
    is_hs = models.CharField(max_length=8)



class Stock_Basic_Company(models.Model):
    ts_code = models.CharField(max_length=12)
    exchange = models.CharField(max_length=8)
    chairman = models.CharField(max_length=30)
    manager = models.CharField(max_length=30)
    secretary = models.CharField(max_length=30)
    reg_capital = models.CharField(max_length=20)
    setup_date = models.CharField(max_length=12)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    introduction = models.CharField(max_length=255)
    website = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    office = models.CharField(max_length=30)
    employees = models.CharField(max_length=50)
    main_business = models.CharField(max_length=255)
    business_scope = models.CharField(max_length=50)