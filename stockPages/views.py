from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


# def index(request):
#     return render_to_response('index.html')


@csrf_exempt
def login(request):
    print(request)
    # email = request.POST['email']
    # password = request.POST['password']
    # print(request.GET['email'])
    # print(request.GET['password'])
    me = 'mxxct'
    # return HttpResponseRedirect('/stockPages/login/')
    return render(request, 'index.html', {'me': me})
    # return render_to_response('index.html')


def to_login(request):
    return render_to_response('login.html')