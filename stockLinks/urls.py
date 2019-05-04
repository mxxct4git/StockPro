from django.conf.urls import url

from django.urls import path

from . import views, tests

app_name = 'stockLinks'

urlpatterns = [
    # http://127.0.0.1:8000/stockLinks/hello/ 是找到对应的APP下的urlpatterns,从而找到对应的view
    url('hello/', views.hello),
    url('test_db/', tests.test_db),
]