from django.shortcuts import render, render_to_response
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world!")

