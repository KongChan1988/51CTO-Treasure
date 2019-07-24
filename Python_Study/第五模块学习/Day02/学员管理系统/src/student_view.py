# -*- coding:utf-8 -*-
# Author:D.Gray
from database.create_table import Class,Teacher,Student,class_m2m_lesson,class_m2m_student,Lesson,Study_record
import sqlalchemy
from sqlalchemy import func
class Student_view(object):
    def __init__(self,session):
        self.session = session
        self.authentication()
        self.handle()

    def authentication(self):
        while True:
            student_input = input("\033[33;0m请输入学生名:\033[0m").strip().capitalize()
            self.student_obj = self.session.query(Student).filter(Student.stu_name == student_input).first()
            if self.student_obj:
                print('\033[32;0m学生ID：%s\n所属班级：%s\033[0m'%(self.student_obj.stu_id,self.student_obj.class_keys))
                break
            else:
                print("\33[31;1m输入错误：请输入有效的学生名\33[0m")
                continue


    def handle(self):
        while True:
            print("\033[35;1m欢迎【%s】进入学员管理系统\n"
                  "1、上传作业\n"
                  "2、查看作业成绩\n"
                  "3、查看班级排名\n"
                  "exit 退出管理系统\n\033[0m" % self.student_obj.stu_name)
            user_func = input("\033[34;0m请输入进行操作的命令:\033[0m")
            self.dic = {
                '1':self.up_homework,
                '2':self.show_homework,
                '3':self.show_rank,
                'exit':self.exit
            }
            if user_func in self.dic.keys():
                self.dic[user_func]()
            else:
                print("\033[31;0m请输入有效操作的命令\033[0m")


    def up_homework(self):
        #print('in the up_homework')
        class_name = input("\033[33;0m请输入班级名:\033[0m").capitalize().strip()
        class_obj = self.student_obj.class_keys
        for classes in class_obj:
            if classes.class_name == class_name:
                if class_name:                           #判断学生是否存在所输入班级中
                    lesson_name = input("\033[33;0m请输入课节名:\033[0m").capitalize().strip()
                    lesson_obj = self.session.query(Lesson).filter(Lesson.lesson_name == lesson_name).first()
                    if lesson_obj:
                        class_m2m_lesson_obj = self.session.query(class_m2m_lesson).filter(
                            class_m2m_lesson.class_id == classes.class_id
                        ).filter(class_m2m_lesson.lesson_id == lesson_obj.lesson_id).first()
                        if class_m2m_lesson_obj:
                            study_record_obj = self.session.query(Study_record).filter(
                                Study_record.class_m2m_lesson_id==class_m2m_lesson_obj.id
                            ).filter(Study_record.stu_id==self.student_obj.stu_id).first()

                            if study_record_obj:
                                if study_record_obj.status == 'N':
                                    print('\033[32;0m作业提交情况：未提交\033[0m' )
                                    up_input = input('\033[33;0m您本次课节作业是否选择提交(Y/N)>>>:\033[0m')\
                                        .strip().capitalize()
                                    if up_input == 'Y':
                                        study_record_obj.status = up_input
                                        self.session.commit()
                                        print('\033[32;0m本次课节作业提交完成\033[0m')
                                    else:
                                        print('\033[31;0m请按时提交本次课节作业\033[0m')
                                        break
                                else:
                                    print('\033[32;0m您本次课节作业情况：已提交\033[0m')
                            else:
                                print("\033[31;1m系统错误：未有该上课记录\033[0m")
                        else:
                            print("\033[31;1m系统错误：class_m2m_lesson表未创建\033[0m")
                    else:
                        print("\33[31;1m系统错误：课节未创建\33[0m")
            else:
                print("\33[31;1m输入错误：班级不存在或学生不在此班级\33[0m")


    def show_homework(self):
        class_name = input("\033[33;0m请输入班级名:\033[0m").capitalize().strip()
        class_obj = self.student_obj.class_keys
        for classes in class_obj:
            if classes.class_name == class_name:
                if class_name:  # 判断学生是否存在所输入班级中
                    lesson_name = input("\033[33;0m请输入课节名:\033[0m").capitalize().strip()
                    lesson_obj = self.session.query(Lesson).filter(Lesson.lesson_name == lesson_name).first()
                    if lesson_obj:
                        class_m2m_lesson_obj = self.session.query(class_m2m_lesson).filter(
                            class_m2m_lesson.class_id == classes.class_id
                        ).filter(class_m2m_lesson.lesson_id == lesson_obj.lesson_id).first()
                        if class_m2m_lesson_obj:
                            study_record_obj = self.session.query(Study_record).filter(
                                Study_record.class_m2m_lesson_id == class_m2m_lesson_obj.id
                            ).filter(Study_record.stu_id == self.student_obj.stu_id).first()

                            if study_record_obj:
                                if study_record_obj.status == 'N':
                                    print('\033[32;0m作业提交情况：未提交\033[0m')
                                    print('\033[31;0m请按时提交本次课节作业\033[0m')
                                else:
                                    print('\033[32;0m本次课节作业成绩：【%s】分\033[0m'%study_record_obj.score)
                                    break
                            else:
                                print("\033[31;1m系统错误：未有该上课记录\033[0m")
                        else:
                            print("\033[31;1m系统错误：class_m2m_lesson表未创建\033[0m")
                    else:
                        print("\33[31;1m系统错误：课节未创建\33[0m")
            else:
                print("\33[31;1m输入错误：班级不存在或学生不在此班级\33[0m")

    def show_rank(self):
        class_name = input("\033[33;0m请输入班级名:\033[0m").capitalize().strip()
        class_obj = self.student_obj.class_keys
        for classes in class_obj:
            if classes.class_name == class_name:
                if class_name:  # 判断学生是否存在所输入班级中
                    lesson_name = input("\033[33;0m请输入课节名:\033[0m").capitalize().strip()
                    lesson_obj = self.session.query(Lesson).filter(Lesson.lesson_name == lesson_name).first()
                    if lesson_obj:
                        class_m2m_lesson_obj = self.session.query(class_m2m_lesson).filter(
                            class_m2m_lesson.class_id == classes.class_id
                        ).filter(class_m2m_lesson.lesson_id == lesson_obj.lesson_id).first()
                        if class_m2m_lesson_obj:
                            study_record_obj = self.session.query(Study_record).filter(
                                Study_record.class_m2m_lesson_id == class_m2m_lesson_obj.id
                            ).filter(Study_record.stu_id == self.student_obj.stu_id).first()

                            if study_record_obj:
                                if study_record_obj.status == 'N':
                                    print('\033[32;0m作业提交情况：未提交\033[0m')
                                    print('\033[31;0m请按时提交本次课节作业\033[0m')
                                else:
                                    print('\033[32;0m本次课节作业成绩：【%s】分\033[0m' % study_record_obj.score)

                                    study_score_obj = self.session.query(Study_record.stu_id,Study_record.score).filter(
                                        Study_record.score>0
                                    ).filter(Study_record.class_m2m_lesson_id == class_m2m_lesson_obj.id)\
                                        .order_by(Study_record.score.desc()).all()
                                    for study_score in study_score_obj:
                                        student_obj = self.session.query(Student).\
                                            filter(Student.stu_id == study_score.stu_id).first()
                                        print('%s   成绩：【%s】分'%(student_obj.stu_name,study_score.score))

                            else:
                                print("\033[31;1m系统错误：未有该上课记录\033[0m")
                        else:
                            print("\033[31;1m系统错误：class_m2m_lesson表未创建\033[0m")
                    else:
                        print("\33[31;1m系统错误：课节未创建\33[0m")
            else:
                print("\33[31;1m输入错误：班级不存在或学生不在此班级\33[0m")

    def exit(self):
        exit('\033[31;0m感谢使用管理系统,\033[0m')