# -*- coding: utf-8 -*-

from django.test import TestCase

# Create your tests here.

import tushare as ts
import pandas as pd
from django.http import HttpResponse
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/stockpro')

#  QQ群：658562506

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

pro = ts.pro_api("9da1aed5b1e4b7a0e022279a8b78e17f7cccf51e4900fb9e95678222")


def test_db(request):
    b = pro.query('trade_cal', exchange='', start_date='20190101', end_date='20190504',
                  fields='exchange,cal_date,is_open,pretrade_date')
    data = b['data']
    columns = data['fields']
    items = data['items']
    res = pd.DataFrame(items, columns=columns)
    # print(res)
    # index =false 是不展示dataframe的index列  if_exists ‘append’代表 表存在即追加，‘replace’代表重建
    res.to_sql('stockdatabase_stock_basic_trade_cal', engine, if_exists='append', index=False)
    return HttpResponse("交易日历写入数据成功")
