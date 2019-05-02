# -*- coding: utf-8 -*-

import tushare as ts
import pandas as pd

#  QQ群：658562506

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

pro = ts.pro_api("9da1aed5b1e4b7a0e022279a8b78e17f7cccf51e4900fb9e95678222")

# 股票列表接口
# 查询当前所有正常上市交易的股票列表，获取基础信息数据，包括股票代码、名称、上市日期、退市日期等
# a = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
# print(a)

# 交易日历接口
# 获取各大交易所交易日历数据， 默认提取的是上交所
# exchange: SSE上交所 SZSE深交所
# b = pro.trade_cal(exchange='', start_date='20190411', end_date='20190502')
# b = pro.query('trade_cal', exchange='', start_date='20190411', end_date='20190502')
# print(b)

# 上市公司基本信息接口
# exchange: SSE上交所 SZSE深交所
# c = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
# c = pro.query('stock_company', exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
# print(c)

# IPO新股列表接口
# d = pro.new_share(start_date='20190401', end_date='20190501')
# d = pro.query('new_share', start_date='20190420', end_date='20190425')
# print(d.T)

# 日线行情接口
# 更新时间：交易日每天15点～16点之间
# e = pro.query('daily', ts_code='002493.SZ', start_date='20190429', end_date='20190430')
# print(e)

# 周线行情接口
# 需要积分300以上
# f = pro.weekly(ts_code='002493.SZ', start_date='20190401', end_date='20190501', fields='ts_code,trade_date,open,high,low,close,vol,amount')
# print(f)
# print(f['data'])
# print(f['data']['fields'])
# # print(f['data']['fields'][1])
# for i in range(len(f['data']['fields'])):
#     print(f['data']['fields'][i])
#
#
# data = f['data']
# columns = data['fields']
# items = data['items']
# res = pd.DataFrame(items, columns=columns)
# print(res)


# 月线行情接口
# 需要积分300以上
# g = pro.query('monthly', ts_code='002493.SZ', start_date='20190101', end_date='20190502', fields='ts_code,trade_date,open,high,low,close,vol,amount')
# g = pro.monthly(ts_code='002493.SZ', start_date='20190101', end_date='20190502', fields='ts_code,trade_date,open,high,low,close,vol,amount')
# print(g)

# 每日指标接口
# 更新时间：交易日每日15点～17点之间
# 需要积分300以上
# h = pro.query('daily_basic', ts_code='002493.SZ', trade_date='20190428',fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')
# print(h['code']) # code：-2002 是权限问题即积分不够

# 停复牌信息接口
# i = pro.query('suspend', ts_code='', suspend_date='20190430', resume_date='', fields='ts_code,suspend_date,resume_date,ann_date,suspend_reason,reason_type')
# data = i['data']
# columns = data['fields']
# items = data['items']
# res = pd.DataFrame(items, columns=columns)
# print(res)

# 个股资金流向接口