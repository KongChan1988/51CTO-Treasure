from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("index")

def detail(request,nid):
    pass

# def detail_x(request,*args,**kwargs):
#     pass
