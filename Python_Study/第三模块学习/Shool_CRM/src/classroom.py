#-*- Coding:utf-8 -*-
# Author: D.Gray
class Classroom(object):
    '''
    班级名称、课程，学生
    '''
    def __init__(self,class_name,course_obj):
        self.class_name = class_name
        self.course_obj = course_obj
        self.class_strdent = {}