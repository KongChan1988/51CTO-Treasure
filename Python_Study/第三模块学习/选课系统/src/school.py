# -*- coding:utf-8 -*-
# Author:D.Gray
import os
from src.course import Course
from src.classroom import Classroom
from src.teacher import Teacher
from src.student import Student

class School(object):
    def __init__(self,sch_name,sch_addr):
        self.sch_name = sch_name
        self.sch_addr = sch_addr
        self.sch_teacher = {}
        self.sch_classroom = {}
        self.sch_course = {}
        self.sch_student = {}

    def create_course(self,course_name,course_price,course_time):
        #创建课程对象
        #根据课程名称为key，课程对象为value来建立对应关系
        sch_course_obj = Course(course_name,course_price,course_time)
        self.sch_course[course_name] = sch_course_obj

    def show_course(self):
        for course_key in self.sch_course:
            show_course_obj = self.sch_course[course_key]
            print("课程名称【%s】\t课程价格【%s】\t课程周期【%s】"
                  % (show_course_obj.course_name,show_course_obj.course_price,show_course_obj.course_time))

    # def modify_course(self,**kwargs):
    # 根据key取出课程对象
    # for course in self.sch_course:
    #     course_obj = self.sch_course[course]
    # 修改course_obj的每个值
    # 保存

    def create_classroom(self,claroom_name,course_obj):
        sch_classroom_obj = Classroom(claroom_name,course_obj)
        self.sch_classroom[claroom_name] = sch_classroom_obj

    def show_classroom(self):
        for claroom_key in self.sch_classroom:
            show_claroom_obj = self.sch_classroom[claroom_key]
            print("班级名称【%s】\t班级课程【%s】\t课程周期【%s】"%(show_claroom_obj.cls_name,
                                                    show_claroom_obj.cls_course_obj.course_name,
                                                  show_claroom_obj.cls_course_obj.course_time))

    def create_teacher(self,sch_tea_name,sch_tea_sal,tea_class_name,class_obj):
        sch_teacher_obj = Teacher(sch_tea_name,sch_tea_sal)
        sch_teacher_obj.add_tea_class(tea_class_name,class_obj)
        self.sch_teacher[sch_tea_name] = sch_teacher_obj

    def show_teacher(self):
        for show_teacher_key in self.sch_teacher:
            show_teacher_obj = self.sch_teacher[show_teacher_key]
            class_list = []
            for tea_class_key in show_teacher_obj.tea_class:
                class_list.append(tea_class_key)
            print("讲师名称【%s】讲师薪资【%s】关联班级【%s】"
                  %(show_teacher_obj.tea_name,
                    show_teacher_obj.tea_sal,class_list))

    def update_teacher(self,update_tea_name,update_class_name,update_class_obj):
        update_teacher_obj = self.sch_teacher[update_tea_name]
        update_teacher_obj.add_tea_class(update_class_name,update_class_obj)

    def create_student(self,sch_stu_name,sch_stu_age,sch_stu_sex,cls_name):
        sch_stu_obj = Student(sch_stu_name,sch_stu_age,sch_stu_sex)
        self.sch_student[sch_stu_name] = sch_stu_obj

        stu_cls_obj = self.sch_classroom[cls_name]
        self.sch_classroom[cls_name] = sch_stu_obj

    def show_tea_clsinfo(self,tea_name):
        show_teainfo_obj = self.sch_teacher[tea_name]
        for cls_info in show_teainfo_obj.teacher_clss:
            cls_info_obj = self.sch_classroom[cls_info]
            stu_list = []
            for stu_info in cls_info_obj.cls_stu:
                stu_list.append(stu_info)
            print('班级【%s】\t关联课程【%s】\t学员【%s】'%(cls_info_obj.cls_name,cls_info_obj.cls_course,stu_list))





