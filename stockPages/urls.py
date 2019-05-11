from django.conf.urls import url

from django.urls import path

from . import views

app_name = 'stockPages'

urlpatterns = [
    # http://127.0.0.1:8000/stockPages/test/ 是找到对应的APP下的urlpatterns,从而找到对应的view
    url('get_stock_index/', views.get_stock_index),  # 实时获取大盘指数指标数据
    url('get_self_manage/', views.get_self_manage),  # 获取上市股票列表
]