# -*- coding:utf-8 -*-
# Author:D.Gray
class Classroom(object):
    def __init__(self,cls_name,cls_course_obj):
        self.cls_name = cls_name
        self.cls_course_obj = cls_course_obj
        self.cls_student = {}