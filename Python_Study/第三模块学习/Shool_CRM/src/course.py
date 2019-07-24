#-*- Coding:utf-8 -*-
# Author: D.Gray

class Course(object):
    '''
    课程名称、课程价格、课程周期
    '''
    def __init__(self,course_name,course_price,course_time):
        self.course_name = course_name
        self.course_price = course_price
        self.course_time = course_time