# -*- coding: utf-8 -*-

from django.test import TestCase

# Create your tests here.

import tushare as ts
import pandas as pd
import time
from django.http import HttpResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from stockDataBase.models import Stock_Basic_Trade_Cal as basic_trade_cal

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/stockpro?charset=utf8')

#  QQ群：658562506

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

pro = ts.pro_api("9da1aed5b1e4b7a0e022279a8b78e17f7cccf51e4900fb9e95678222")

# 增
def test_db(request):
    # 可以设置一个周期，比如每七天把下一个周的时间放入到参数添加到数据库中
    b = pro.query('trade_cal', exchange='', start_date='20190502', end_date='20190504',
                  fields='exchange,cal_date,is_open,pretrade_date')
    data = b['data']
    columns = data['fields']
    items = data['items']
    res = pd.DataFrame(items, columns=columns)
    print(res)
    # index =false 是不展示dataframe的index列  if_exists ‘append’代表 表存在即追加，‘replace’代表重建
    # res.to_sql('stockdatabase_stock_basic_trade_cal', engine, if_exists='append', index=False)
    return HttpResponse("交易日历写入数据成功")


def operate_datebase(request):
    # 查
    # table.objects.all()
    # all()返回的是QuerySet对象，程序并没有真的在数据库中执行SQL语句查询数据，但支持迭代，使用for循环可以获取数据。
    # values()返回的是QuerySet对象，set中包含了具体的数值。
    # table.objects.get(id='1')
    # get()返回的是Model对象，类型为列表，说明使用get方法会直接执行sql语句获取数据
    # filter()和get()类似，但支持更强大的查询功能

    res = basic_trade_cal.objects.values()[:5]
    print(res)
    # for item in res:
    #     print(item.exchange)
    #     print(item.cal_date)
    #     print(item.is_open)
    #     print(item.pretrade_date)

    df = pd.DataFrame(list(res))
    print(df)

    return HttpResponse("测试数据库成功")

