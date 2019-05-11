# -*- coding: utf-8 -*-

from django.test import TestCase

# Create your tests here.

import tushare as ts
import pandas as pd
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from sqlalchemy import create_engine
from stockDataBase.models import Stock_Basic_Trade_Cal as basic_trade_cal
from stockDataBase.models import Stock_Basic_List as basic_list

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/stockpro?charset=utf8')

#  QQ群：658562506

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

pro = ts.pro_api("9da1aed5b1e4b7a0e022279a8b78e17f7cccf51e4900fb9e95678222")

# 增
def test_db_trade_cal(request):
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


# 增
def test_db_list(request):
    # 加一个定时任务先truncate原先所有的数据 再追加
    a = pro.query('stock_basic', exchange='', list_status='L',
                  fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
    data = a['data']
    columns = data['fields']
    items = data['items']
    res = pd.DataFrame(items, columns=columns)
    # print(res)
    # index =false 是不展示dataframe的index列  if_exists ‘append’代表 表存在即追加，‘replace’代表重建
    res.to_sql('stockdatabase_stock_basic_list', engine, if_exists='append', index=False)
    return HttpResponse("股票列表写入数据成功")


def operate_db(request):
    # 查
    # table.objects.all()
    # all()返回的是QuerySet对象，程序并没有真的在数据库中执行SQL语句查询数据，但支持迭代，使用for循环可以获取数据。
    # values()返回的是QuerySet对象，set中包含了具体的数值。
    # table.objects.get(id='1')
    # get()返回的是Model对象，类型为列表，说明使用get方法会直接执行sql语句获取数据
    # filter()和get()类似，但支持更强大的查询功能

    # res = basic_trade_cal.objects.values()[:5]
    res = basic_list.objects.values()
    print(res)
    # for item in res:
    #     print(item.exchange)
    #     print(item.cal_date)
    #     print(item.is_open)
    #     print(item.pretrade_date)

    df = pd.DataFrame(list(res))
    print(df)

    return HttpResponse("测试数据库成功")


def send_email(request):
    # 一个收件人
    # send_mail('test_03', '发送第3个测试邮件', 'mxxct <386965035@qq.com>',
    #           ['liufangtong@enn.cn'], fail_silently=False)

    # 多个收件人
    # message1 = ('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
    # message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
    # send_mass_mail((message1, message2), fail_silently=False)

    # send_mail 每次发邮件都会建立一个连接，发多封邮件时建立多个连接。而 send_mass_mail 是建立单个连接发送多封邮件，所以一次性发送多封邮件时 send_mass_mail 要优于 send_mail

    # 发送带附件的 html 格式的内容
    from_email = settings.DEFAULT_FROM_EMAIL
    # subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
    msg = EmailMultiAlternatives("test_1423","测试html格式邮件",from_email, ['liufangtong@enn.cn','zhangjiahaoa@enn.cn'])

    msg.content_subtype = 'html'

    # 添加附件
    # msg.attach_file('./static/img/panda.ico')
    msg.attach_file('G:/工作/新奥/文件/大数据赋能群汇总文件/考勤汇总/出差.txt')

    # 发送
    msg.send()

    return HttpResponse("测试发送邮件")