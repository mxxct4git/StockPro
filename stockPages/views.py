from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
import pandas as pd
import datetime
import stockDataBase.models as models

# Create your views here.


@csrf_exempt
def login(request):
    # print(request)
    vUsername = request.POST['username']
    vPassword = request.POST['password']
    res = models.Stock_Basic_User.objects.filter(username=vUsername, password=vPassword)\
        .values('id', 'username', 'password', 'truename', 'email', 'authority', 'deleted')  # QuerySet 类型

    df = pd.DataFrame(list(res))
    # print(df)
    vTruename = df['truename'][0]
    vAuthority = df['authority'][0]
    vUserId = df['id'][0]
    # print(type(vTruename))
    # print(vAuthority)
    # print(type(vUserId))
    # 在session中存储用户已经登录的记录，无需再二次登录
    session_user_login_key = str(vUserId) + '_login'
    request.session[session_user_login_key] = 'Y'
    # 在session中存储当前登录用户的基本信息
    session_user_info_key = str(vUserId) + '_user'
    request.session[session_user_info_key] = serializers.serialize('json', models.Stock_Basic_User.objects.filter(username=vUsername, password=vPassword))
    # 删除 session
    # del request.session[key]  # 不存在时报错
    tmp = request.session.get(session_user_info_key, default=None)  # str 类型
    # print(tmp)
    # print(type(tmp))
    even = json.loads(tmp)  # list 类型
    # print(type(even))
    # print(even[0])
    # print(even[0]['fields'])
    # print(even[0]['fields']['truename'])
    # print(even)
    # print(even[0])
    # print(even[1])
    # return HttpResponseRedirect('/stockPages/login/')
    return render(request, 'index.html', {'me': vTruename, 'userId': vUserId, 'auth': vAuthority})
    # return render_to_response('index_old.html')


@csrf_exempt
def to_login(request):
    print(request)
    raw_url = request.get_raw_uri()
    if 'id' in raw_url:
        # 如果参数中有 id 说明该用户已经登录
        vUserId = raw_url.split("_")[2]
        session_user_info_key = str(vUserId) + '_user'
        vTmp = request.session.get(session_user_info_key, default=None)  # str 类型
        vRes = json.loads(vTmp)
        vTruename = vRes[0]['fields']['truename']
        return render(request, 'index.html', {'me': vTruename, 'userId': vUserId})
    # print(request.GET['true'])
    # 在这里添加判断，传参会传递userid，如果用户已经登录就不会跳转到登录页面
    return render_to_response('login.html')