# -*- coding:utf-8 -*-
# Author:D.Gray
from app02 import views
from app02 import urls
from django.conf.urls import url,include
urlpatterns = [
    url("login/",views.login),
url("index/",views.index),
url("logout/",views.logout),
url("test/",views.test),
url("sigin/",views.sigin),
url("cache/",views.cache),
]