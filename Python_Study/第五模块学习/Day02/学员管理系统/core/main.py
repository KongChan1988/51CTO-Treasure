# -*- coding:utf-8 -*-
# Author:D.Gray
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from conf.setting import engine
from src.teacher_view import Teacher_view
from src.student_view import Student_view
from database.create_table import Teacher,Class

class Action(object):
    def __init__(self):
        Session_class = sessionmaker(bind=engine)
        self.session= Session_class()
        self.initialize_database()

    def func(self):
        while True:
            print("\033[36;1m欢迎进入CLASS_SYSTEM系统\n"
                  "1 讲师视图\n"
                  "2 学生视图\n"
                  "q 退出管理系统\n\033[0m")
            user_choice = input("\033[34;0m请输入你进入的视图:\033[0m")
            if user_choice == '1':
                Teacher_view(self.session)
            elif user_choice == '2':
                Student_view(self.session)
            elif user_choice == 'q':
                print("\033[31;0m感谢使用管理系统\033[0m")
                break
            else:
                print("\033[31;1m请输入正确的选项\033[0m")

    def initialize_database(self):
        '''
        初始化数据库
        :return:
        '''
        result = self.session.query(Teacher).filter(Teacher.teacher_id>0).all()
        #print(result)
        if not result:
            c1 = Class(class_name = 'S14',course = 'Python')
            t1 = Teacher(teacher_name = 'Alex')
            t1.teacher_class = [c1]

            self.session.add_all([c1,t1])
            self.session.commit()
            print('数据添加成功')


