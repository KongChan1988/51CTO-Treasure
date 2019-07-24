#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from io import BytesIO
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from utils.check_code import create_validate_code
from repository import models
from django.core.exceptions import ValidationError
from ..forms import account

def jsonp(request):
    func = request.GET.get('callback')
    content = '%s(100000)' %(func,)
    return HttpResponse(content)


class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field,ValidationError):
            return {"code":field.code,"messages":field.message}
        else:
            return json.JSONEncoder.default(self, field)

def check_code(request):
    """
    验证码
    :param request:
    :return:
    """
    stream = BytesIO()
    img, code = create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())


def login(request):
    """
    登陆
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        result = {'status': False, 'message': None, 'data': None}
        form = account.LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_info = models.UserInfo.objects. \
                filter(username=username, password=password). \
                values('nid', 'nickname',
                       'username', 'email',
                       'avatar',
                       'blog__nid',
                       'blog__site').first()

            if not user_info:
                # result['message'] = {'__all__': '用户名或密码错误'}
                result['message'] = '用户名或密码错误'
            else:
                result['status'] = True
                request.session['user_info'] = user_info
                if form.cleaned_data.get('rmb'):
                    request.session.set_expiry(60 * 60 * 24 * 7)
        else:
            print(form.errors.as_data())
            if 'check_code' in form.errors:
                result['message'] = '验证码错误或者过期'
            else:
                result['message'] = '用户名或密码错误'
        return HttpResponse(json.dumps(result))


def register(request):
    """
    注册
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        res ={"status":False,"message":None,"data":None}
        obj = account.RegisterForm(request=request,data=request.POST)
        print(obj.data)
        if obj.is_valid():
            res["status"] = True
            username = request.POST.get("username")
            pwd = request.POST.get("password")
            email = request.POST.get("email")
            models.UserInfo.objects.create(username=username,password=pwd,email=email)
            res["message"] = "注册成功"
        else:
            error = obj.errors.as_data()
            # print(error)
            for k,v in error.items():
                res["message"] = error[k][0]
        result = json.dumps(res,cls=JsonCustomEncoder)
        return HttpResponse(result)



def logout(request):
    """
    注销
    :param request:
    :return:
    """
    request.session.clear()

    return redirect('/')
