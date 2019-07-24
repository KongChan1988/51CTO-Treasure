# -*- coding:utf-8 -*-
# Author:D.Gray
from app03 import views
from app03 import urls
from django.conf.urls import url,include
urlpatterns = [
    url("login/",views.login),
]
