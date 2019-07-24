#-*- Coding:utf-8 -*-
# Author: D.Gray
class Student(object):
    '''
    学生姓名，性别，年龄
    '''
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = 0

    def modify_score(self,new_score):
        '''
        教师可以修改学生分数
        :param new_score:
        :return:
        '''
        self.new_score = new_score