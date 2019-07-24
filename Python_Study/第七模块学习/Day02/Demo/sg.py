# -*- coding:utf-8 -*-
# Author:D.Gray

from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception
from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate
from django.test.signals import setting_changed
from django.test.signals import template_rendered
from django.db.backends.signals import connection_created

def f1(sender, **kwargs):
    print("xxoo_callback")
    print(sender,kwargs)
pre_init.connect(f1)
# xxoo指上述导入的内容

#定义信号
import django.dispatch
pizza_done = django.dispatch.Signal(providing_args=["toppings","size"])
#自定义信号
def callback(sender,**kwargs):
    print("callback")
    print(sender,kwargs)
pizza_done.connect(callback)