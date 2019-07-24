#-*- Coding:utf-8 -*-
# Author: D.Gray
class Teacher(object):
    '''
    讲师姓名，年龄，性别，工资，所关联的班级
    '''
    def __init__(self,teacher_name,teacher_age,sex,teacher_sal):
        self.teacher_name = teacher_name
        self.teacher_age = teacher_age
        self.sex = sex
        self.teacher_sal = teacher_sal
        self.teacher_classroom = {}

    def add_teacher_classroom(self,class_name,class_obj):
        '''
        讲师和班级进行关联
        :param class_name:
        :param class_obj:
        :return:
        '''
        self.teacher_classroom[class_name] = class_obj