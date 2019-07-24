#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render


def base_info(request):
    """
    博主个人信息
    :param request:
    :return:
    """
    return render(request, 'backend_base_info.html')


def tag(request):
    """
    博主个人标签管理
    :param request:
    :return:
    """
    return render(request, 'backend_tag.html')


def category(request):
    """
    博主个人分类管理
    :param request:
    :return:
    """
    return render(request, 'backend_category.html')


def article(request):
    """
    博主个人文章管理
    :param request:
    :return:
    """
    return render(request, 'backend_article.html')


def add_article(request):
    """
    添加文章
    :param request:
    :return:
    """
    return render(request, 'backend_add_article.html')


def edit_article(request):
    """
    编辑文章
    :param request:
    :return:
    """
    return render(request, 'backend_edit_article.html')