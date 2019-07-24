# -*- coding:utf-8 -*-
# Author:D.Gray
class Teacher(object):
    def __init__(self,tea_name,tea_sal):
        self.tea_name = tea_name
        self.tea_sal = tea_sal
        self.tea_class = {}

    def add_tea_class(self,tea_class_name,tea_class_obj):
        self.tea_class[tea_class_name] = tea_class_obj
