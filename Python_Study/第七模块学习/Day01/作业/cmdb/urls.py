# -*- coding:utf-8 -*-
# Author:D.Gray
from django.urls import path
from django.conf.urls import url,include
from cmdb import views
urlpatterns = [
    path('login/', views.login),
    path('home/',views.home),
    path('orm/', views.rom),
    path('user_info/', views.user_info),
    url('user_info-(?P<nid>\d+)',views.user_detail),
    url('user_delete-(?P<nid>\d+)',views.User_Delete.as_view(),),
    path('user_insert/', views.User_Insert.as_view(),),
]