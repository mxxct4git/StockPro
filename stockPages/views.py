from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import tushare as ts
from django.core import serializers
import json
import pandas as pd
import datetime
import stockDataBase.models as models

# Create your views here.


@csrf_exempt
# 获取大盘指数指标数据
def get_stock_index(request):
    m = ts.get_index()
    print("test*****")
    # print(m)
    # 上证指数
    # vShang_index_open = m['open'][0]  # 开盘点位
    vShang_index_change = m['change'][0]  # 涨跌幅
    # vShang_index_preclose = m['preclose'][0]  # 昨日收盘点位
    vShang_index_now = m['close'][0]  # 收盘点位（即时点位）
    # vShang_index_high = m['high'][0]  # 最高位
    # vShang_index_low = m['low'][0]  # 最低位
    # vShang_index_volume = m['volume'][0]  # 成交量（手）
    # vShang_index_volume = int(vShang_index_volume)
    # vShang_index_amount = m['amount'][0]  # 成交金额（亿元）
    # vShang_index_amount = float(vShang_index_amount)

    # 深证指数
    # vShen_index_open = m['open'][12  # 开盘点位
    vShen_index_change = m['change'][12]  # 涨跌幅
    # vShen_index_preclose = m['preclose'][12]  # 昨日收盘点位
    vShen_index_now = m['close'][12]  # 收盘点位（即时点位）
    # vShen_index_high = m['high'][12]  # 最高位
    # vShen_index_low = m['low'][12]  # 最低位
    # vShen_index_volume = m['volume'][12]  # 成交量（手）
    # vShen_index_volume = int(vShen_index_volume)
    # vShen_index_amount = m['amount'][12]  # 成交金额（亿元）
    # vShen_index_amount = float(vShen_index_amount)

    # Ａ股指数
    vA_index_change = m['change'][1]  # 涨跌幅
    vA_index_now = m['close'][1]  # 收盘点位（即时点位）

    # 综合指数
    vZong_index_change =  m['change'][3]  # 涨跌幅
    vZong_index_now = m['close'][3]  # 收盘点位（即时点位）

    response = JsonResponse({"shang_now": vShang_index_now, 'shang_change': vShang_index_change,
                             'shen_now': vShen_index_now, 'shen_change': vShen_index_change,
                             'a_now': vA_index_now, 'a_change': vA_index_change,
                             'zong_now': vA_index_now, 'zong_change': vZong_index_change})
    return response


@csrf_exempt
def get_self_manage(request):
    res = json.dumps(list(models.Stock_Basic_List.objects.values('id', 'ts_code', 'symbol', 'name')))
    response = JsonResponse(res, safe=False)
    return response