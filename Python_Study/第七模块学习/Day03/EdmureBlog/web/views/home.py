#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from repository import models


def index(request):
    """
    博客首页，展示全部博文
    :param request:
    :return:
    """
    article_list = models.Article.objects.all()
    return render(request, 'index.html', {'article_list': article_list})


def home(request, site):
    """
    博主个人首页
    :param request:
    :param site: 博主的网站后缀如：http://xxx.com/wupeiqi.html
    :return:
    """
    user_home = models.Blog.objects.filter(site=site).select_related('user').first()
    return render(request, 'home.html', {'user_home': user_home})


def filter(request, site, condition, val):
    """
    分类显示
    :param request:
    :param site:
    :param condition:
    :param val:
    :return:
    """
    user_home = models.Blog.objects.filter(site=site).select_related('user').first()
    if not user_home:
        return redirect('/')
    template_name = "home_summary_list.html"
    if condition == 'tag':
        template_name = "home_title_list.html"
        article_list = models.Article.objects.filter(tags__title=val, blog=user_home).all()
    elif condition == 'category':
        article_list = models.Article.objects.filter(category__title=val, blog=user_home).all()
    elif condition == 'date':
        article_list = models.Article.objects.filter(blog=user_home).extra(
            where=['date_format(create_time,"%%Y-%%m")=%s'], params=[val, ]).all()
    else:
        article_list = []

    return render(request, template_name)


def detail(request, site, nid):
    """
    博文详细页
    :param request:
    :param site:
    :param nid:
    :return:
    """
    return render(request, 'home_detail.html')

