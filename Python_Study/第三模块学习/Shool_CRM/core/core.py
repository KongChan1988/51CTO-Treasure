#-*- Coding:utf-8 -*-
# Author: D.Gray
import os,shelve
from conf import settings
from src.classroom import Classroom
from src.course import Course
from src.student import Student
from src.teacher import Teacher
from src.school import School

class Conter(object):
    #退出的标记
    def run(self):
        exit_flag = False
        menu = u'''
            \033[32;1m
            1.学生视图
            2.讲师视图
            3.学习视图
            4.退出\033[0m
        '''
        while True:
            print(menu)
            user_option = input("请输入管理视图...按Q退出>>>:")
            if user_option == "1":
                Student_view()
            elif user_option == "2":
                Teacher_view()
            elif user_option == "3":
                School_view()
            elif user_option.capitalize() == "Q":
                break
            else:
                print("输入的选项不正确,请重新输入")

class School_view(object):
    def __init__(self):
        if os.path.exists(settings.school_file + '.dat'):
            self.school_file = shelve.open(settings.school_file)
            self.school_manager()
            self.school_file.close()
        else:
            print("没有学校和班级的数据，请先创建")
            self.init_school()
            self.school_manager()
            self.school_file.close()

    def init_school(self):
        self.school_file = shelve.open(settings.school_file)
        self.school_file["北京"] = School("北京总校","北京")
        self.school_file["上海"] = School("上海总校","上海")

    def school_manager(self):
        while True:
            for sch_name in self.school_file:
                print("学校名称【%s】"%sch_name)

            sch_option = input("请输入管理的学校").strip()
            if sch_option in self.school_file:
                self.sch_option = sch_option
                self.school_obj = self.school_file[sch_option]

                while True:
                    menu = u'''
                        欢迎来到老男孩【%s】校区
                        1、添加课程  add_course
                        2、添加班级  add_classroom
                        3、添加讲师  add_teacher
                        4、查看班级  show_classroom
                        5、查看课程  show_course
                        6、查看讲师  show_teacher
                        7、退出        exit
                    '''%(sch_name)
                    print(menu)
                    user_choise = input("请选择以上操作").strip()
                    if hasattr(self,user_choise):
                        getattr(self,user_choise)()

    def add_course(self):
        # 输入对象的信息
        # 判断，有课程就提示，没课程就调用school方法去创建
        add_course_name = input("请输入课程名称").strip()
        add_course_price = input("请输入课程价格").strip()
        add_course_time = input("请输入课程周期").strip()
        if add_course_name in self.school_obj.sch_course:
            print("该课程已存在")
        else:
            self.school_obj.create_course(add_course_name,add_course_price,add_course_time)
            print("【%s】课程已添加成功"%add_course_name)
            self.school_file.update({self.sch_option:self.school_obj})

    def add_classroom(self):
        #输入对象的信息
        #判断班级不存在且课程存在，才可以创建新班级
        #否则提示爆粗
        cls_name = input("请输入班级名称").strip()
        cls_course = input("请输入课程").strip()
        if cls_name not in self.school_obj.sch_classroom:
            if cls_name in self.school_obj.sch_course:
                course_obj = self.school_obj.sch_course[cls_course]
                self.school_obj.create_class(cls_name,cls_course)
                self.school_file.update({self.sch_option:self.school_obj})
                print("班级创建成功")
            else:
                print("课程不存在")
        else:
            print("班级不存在")

    def add_teacher(self):
        teach_name = input("请输入讲师名称")
        teach_age = input("请输入讲师年龄")
        teach_sex = input("请输入讲师性别")
        teach_sal = input("请输入讲师工资")
        teach_cls = input("请输入讲师班级")
        if teach_cls in self.school_obj.sch_classroom:
            cls_obj = self.school_obj.sch_classroom[teach_cls]
            if teach_name not in self.school_obj.sch_teacher:
                self.school_obj.create_teacher(teach_name,teach_age,teach_sex
                                               ,teach_sal,teach_cls,cls_obj)
                print("讲师创建成功")
            else:
                self.school_obj.modify_teacher({})
                print("修改讲师信息成")
            self.school_file.update({self.sch_option:self.school_obj})
        else:
            print("请先创建班级")

class Teacher_view(object):
    def __init__(self):
        if os.path.exists(settings.school_file + ".dat"):
            self.school_file = shelve.open(settings.school_file)
            self.teacher_manage()
            self.school_file.close()
        else:
            print("讲师不存在，请先创建学校")
            exit()


class Student_view(object):
    #1.判断是否存在
    #2.输入学校，班级，课程
    #3.验证输入的数据是否存在
    #4.存在更新文件，完成学生的注册
    pass