#-*- Coding:utf-8 -*-
# Author: D.Gray
import os,sys
from src.classroom import Classroom
from src.course import Course
from src.student import Student
from src.teacher import Teacher

class School(object):
    '''
    学习名称，地址，课程，班级，讲师，学生
    '''
    def __init__(self,name,addrs):
        self.name = name
        self.addrs = addrs
        self.sch_course = {}
        self.sch_classroom = {}
        self.sch_teacher = {}
        self.sch_student = {}

    def create_course(self,course_name,course_price,course_time):
        '''
        1:先创建课程对象
        2：根据课程名称为key,课程对象为values来建立对应关系
        :param course_name:
        :param course_price:
        :param course_time:
        :return:
        '''
        courses_obj = Course(course_name,course_price,course_price)
        self.sch_course[course_name] = courses_obj

    def show_course(self):
        for course in self.sch_course:
            course_obj = self.sch_course[course]
            print("课程名称【%s】\t课程价格【%s】\t课程周期【%s】"
                  %(course.course_name,course.course_price,course.course_time))

    #def modify_course(self,**kwargs):
        #根据key取出课程对象
        # for course in self.sch_course:
        #     course_obj = self.sch_course[course]
        #修改course_obj的每个值
        #保存

    def create_classroom(self,class_name,course_obj):
        class_obj = Classroom(class_name,course_obj)
        self.sch_classroom[class_name] = course_obj

    def show_classroom(self):
        for classroom in self.sch_classroom:
            cls_obj = self.sch_classroom[classroom]
            print("班级名称【%s】\t班级课程【%s】"%(classroom.class_name,classroom.course_obj))

    # def modify_classroom(self,**kwargs):
    # 根据key取出课程对象
    # for course in self.sch_course:
    #     course_obj = self.sch_course[course]
    # 修改course_obj的每个值
    # 保存

    def crent_teacher(self,teach_name,teach_age,teach_sex,
                      teach_sal,cls_name,cls_obj):
        teacher_obj = Teacher(teach_name,teach_age,teach_sex,teach_sal)
        teacher_obj.add_teach_classroom(cls_name,cls_obj)
        self.sch_teacher[teach_name] = teacher_obj

    def show_teacher(self):
        pass

    def modify_teacher(self,**kwargs):
        pass

    def crent_student(self,stu_name,stu_age,stu_sex,cls_name):
        #创建学生对象
        student_obj = Student(stu_name,stu_age,stu_sex)
        self.sch_student[stu_name] = student_obj
        #建立学生和班级的对应关系
        class_obj = self.sch_classroom[cls_name]
        class_obj.class_student[stu_name] = student_obj
        #更新班级信息
        self.sch_classroom[cls_name] = class_obj

    def show_teacher_stu_info(self,teach_name):
        teacher_obj = self.sch_teacher[teach_name]
        for t in teacher_obj.teach_classroom:
            cls_obj = self.sch_classroom[t]
            stu_list = []
            for j in cls_obj.class_student:
                stu_list.append(j)
            print("班级名称【%s】\t课程【%s】\t学生【%s】"
                  %(cls_obj.class_name,cls_obj.course_obj.course_name,
                    stu_list))

    def modify_sutdent_score(self,teach_name,stu_name,new_score):
        #1.查查该讲师所对的班级
        #2.查查该班级的学生
        #3.输入学生姓名，如果存在，则调用modify_score方法进行修改
        pass
