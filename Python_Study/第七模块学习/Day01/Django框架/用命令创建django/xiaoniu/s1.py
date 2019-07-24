#-*-coding:utf-8 -*-
# Author: D.Gray
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("我的第一个django框架")
    # return HttpResponse("OK")