from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render_to_response('index.html')


def login(request):
    print(request.GET)
    print(request.GET['id'])
    print(request.GET['password'])
    return render_to_response('login.html')