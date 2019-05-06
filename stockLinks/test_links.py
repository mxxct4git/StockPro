# -*- coding: utf-8 -*-

import tushare as ts
import pandas as pd
import time
import datetime

#  QQ群：658562506

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

pro = ts.pro_api("9da1aed5b1e4b7a0e022279a8b78e17f7cccf51e4900fb9e95678222")

# 测试时间获取并格式化
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）

# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

print(time.localtime())
print(time.time())
print(time.strftime('%Y%m%d', time.localtime()))
#  因为需要对时间进行加减，所以使用 datetime 包
print(datetime.datetime.now())
# 格式化的方式和 time 包的方式一致
print(datetime.datetime.now().strftime('%Y%m%d'))
# 加减法使用 timedelta
print((datetime.datetime.now() + datetime.timedelta(days=7)).strftime('%Y%m%d'))

# 股票列表接口
# 查询当前所有正常上市交易的股票列表，获取基础信息数据，包括股票代码、名称、上市日期、退市日期等
# ts_code,symbol,name,area,induy,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs
# a = pro.query('stock_basic', exchange='', list_status='', fields='ts_code,symbol,name,area,induy,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
# a = pro.query('stock_basic', exchange='SSE', list_status='P', fields='ts_code,symbol,name,area,industry,list_date')
# print(len(a['data']['items']))
# data = a['data']
# columns = data['fields']
# items = data['items']
# res = pd.DataFrame(items, columns=columns)
# print(res)
# print(a)

# 交易日历接口
# 获取各大交易所交易日历数据， 默认提取的是上交所
# exchange: SSE上交所 SZSE深交所
# b = pro.trade_cal(exchange='', start_date='20190411', end_date='20190502')
# b = pro.query('trade_cal', exchange='', start_date='20190101', end_date='20190501', fields='exchange,cal_date,is_open,pretrade_date')
# data = b['data']
# columns = data['fields']
# items = data['items']
# res = pd.DataFrame(items, columns=columns)
# print(res)

# 上市公司基本信息接口
# exchange: SSE上交所 SZSE深交所
# ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope
# c = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
# c = pro.query('stock_company', exchange='SSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
# print(len(c['data']['items']))

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
# 需要积分1500以上
# 获取沪深A股票资金流向数据，分析大单小单成交情况，用于判别资金动向
# j = pro.query('moneyflow', ts_code='002493.SZ', start_date='20190415', end_date='2019025')
# print(j['code'])

# 利润表接口
# l = pro.query('income',ts_code='002493.SH', start_date='20190401', end_date='20190430', fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,diluted_eps')
# print(l['code'])