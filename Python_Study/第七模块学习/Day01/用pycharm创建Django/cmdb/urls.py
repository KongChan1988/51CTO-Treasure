# -*- coding:utf-8 -*-
# Author:D.Gray
from django.urls import path
from django.contrib import admin
from django.conf.urls import url,include
from cmdb import views
urlpatterns = [
    url('index/',views.index),
    url('detail/',views.detail),
    url('detail-(\d+)-1.html/',views.detail_z),
    url('detail-(?P<nid>\d+).html/',views.detail_x),
]