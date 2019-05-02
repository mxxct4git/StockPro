from django.conf.urls import url

from django.urls import path

from . import views

app_name = 'stockPages'

urlpatterns = [
    # http://127.0.0.1:8000/stockPages/test/ 是找到对应的APP下的urlpatterns,从而找到对应的view
    url('test/', views.test),
]