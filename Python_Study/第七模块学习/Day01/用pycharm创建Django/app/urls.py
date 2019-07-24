# -*- coding:utf-8 -*-
# Author:D.Gray

from django.urls import path
from django.contrib import admin
from django.conf.urls import url,include
from app import views
urlpatterns = [
    url('index/',views.index),
    url('detail-(\d+)/',views.detail),
    # url('detail-(?P<nid>\d+)/',views.detail_x),
]