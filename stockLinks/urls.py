from django.conf.urls import url

from django.urls import path

from . import views, tests

app_name = 'stockLinks'

urlpatterns = [
    # http://127.0.0.1:8000/stockLinks/hello/ 是找到对应的APP下的urlpatterns,从而找到对应的view
    url('to_login/', views.to_login),  # 进入到登录界面
    url('login/', views.login),  # 点击登录跳转到 index.html

    url('to_self_select_manage/', views.to_self_select_manage),  # 跳转到self_select_manage.html
    url('add_self_select/', views.add_self_select),  # 添加自选股


    # url('get_stock_list/', views.get_stock_list),  # 获取大盘指数指标数据


    # Test
    url('test_db_trade_cal/', tests.test_db_trade_cal),
    url('test_db_list/', tests.test_db_list),
    url('operate_db/', tests.operate_db),
    url('send_email/', tests.send_email),
]