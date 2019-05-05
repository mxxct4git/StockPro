"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.views import serve

urlpatterns = {
    path('admin/', admin.site.urls),
    # path(r'panda.ico', RedirectView.as_view(url=r'/static/img/panda.ico')),
    # url(r'^panda.ico$', RedirectView.as_view(url=r'static/img/panda.ico')),  # 网站图标
    # path('panda.ico', serve, {'path': './../static/img/panda.ico'}),

    # http://127.0.0.1:8000/stockLinks/hello/
    # http://127.0.0.1:8000/stockLinks 是找到对应的APP
    # http://127.0.0.1:8000/stockLinks/hello/ 是找到对应的APP下的urlpatterns,从而找到对应的views
    path('stockLinks/', include('stockLinks.urls')),
    path('stockPages/', include('stockPages.urls')),
}
