from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import stockDataBase.models as models
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


# def index(request):
#     return render_to_response('index.html')


@csrf_exempt
def login(request):
    print(request)
    vUsername = request.POST['username']
    vPassword = request.POST['password']
    print(vUsername)
    print(vPassword)
    res = models.Stock_Basic_User.objects.filter(username=vUsername, password=vPassword)\
        .values('id', 'username', 'password', 'truename', 'email', 'authority', 'deleted')

    df = pd.DataFrame(list(res))
    print(df)
    vTruename = df['truename'][0]
    print(vTruename)
    # return HttpResponseRedirect('/stockPages/login/')
    return render(request, 'index.html', {'me': vTruename})
    # return render_to_response('index.html')


def to_login(request):
    return render_to_response('login.html')