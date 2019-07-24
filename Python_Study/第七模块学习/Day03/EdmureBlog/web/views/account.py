#!/usr/bin/env python
# -*- coding:utf-8 -*-
from io import BytesIO
from django.shortcuts import HttpResponse
from django.shortcuts import render
from utils.check_code import create_validate_code


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
    if request.method == "POST":
        if request.session['CheckCode'].upper() == request.POST.get('check_code').upper():
            pass
        else:
            print('验证码错误')


    return render(request, 'login.html')


def register(request):
    """
    注册
    :param request:
    :return:
    """
    return render(request, 'register.html')


def logout(request):
    """
    注销
    :param request:
    :return:
    """
    pass
