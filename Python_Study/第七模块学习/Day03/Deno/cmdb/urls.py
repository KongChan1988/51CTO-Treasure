# -*- coding:utf-8 -*-
# Author:D.Gray
from cmdb.views import login
from django.conf.urls import url,include
urlpatterns = [
    url("login/",login.login),
url("register/",login.Register),
url("login_ajax/",login.login_ajax),
url("user_list/",login.user_list),
url("user_edit-(\d+)/",login.user_edit),
url("upload/",login.upload),
url("upload_file/",login.upload_file),
]