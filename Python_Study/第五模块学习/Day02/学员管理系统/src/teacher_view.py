# -*- coding:utf-8 -*-
# Author:D.Gray
from database.create_table import Class,Teacher,Student,class_m2m_lesson,class_m2m_student,Lesson,Study_record
class Teacher_view(object):
    def __init__(self,session):
        print('in the teacher_view')
        self.session = session
        self.authentication()
        self.handle()

    def authentication(self):
        '''
        教师认证函数
        :return:
        '''
        while True:
            teacher_input = input("\033[34;0m请输入讲师名:\033[0m").strip()
            self.teacher_obj = self.session.query(Teacher).filter(Teacher.teacher_name == teacher_input).first()
            #print(teacher_obj)
            if self.teacher_obj is None:
                print("\33[31;1m输入错误：请输入有效的讲师名\33[0m")
                continue
            else:
                break

    def handle(self):
        '''
        教师操作视图
        :return:
        '''
        while True:
            print("\033[35;1m欢迎【%s】进入讲师管理系统\n"
                  "1、显示可管理的班级\n"
                  "2、创建班级\n"
                  "3、添加学员\n"
                  "4、添加课程节次\n"
                  "5、创建上课记录\n"
                  "6、修改学员成绩\n"
                  "exit 退出管理系统\n\033[0m"%self.teacher_obj.teacher_name)
            self.dic = {
                '1':self.show_classes,
                '2':self.add_class,
                '3':self.add_student,
                '4':self.add_lesson,
                '5':self.add_study_record,
                '6':self.modify_scores,
                'exit':self.exit
            }
            action_input = input("\033[34;0m请输入进行操作的命令:\033[0m")
            if action_input in self.dic.keys():
               self.dic[action_input]()
            else:
                print("\033[31;0m请输入有效操作的命令\033[0m")

    def show_classes(self):
        '''
        查看所有管理的班级
        :return:
        '''
        for class_obj in self.teacher_obj.teacher_class:
            print('\033[32;1m%s  班级名：%s   课程：%s\033[0m'
                  % (self.teacher_obj.teacher_name, class_obj.class_name, class_obj.course))

    def add_class(self):
        '''
        添加教室
        :return:
        '''
        class_input = input("\033[33;0m请输入创建班级的名称:\033[0m").capitalize()
        class_obj = self.session.query(Class).filter(Class.class_name==class_input).first()
        if class_obj is None:
            course_input = input("\033[33;0m请输入创建班级的课程:\033[0m").capitalize()
            class_obj =  Class(class_name = class_input,course = course_input)
            self.teacher_obj.teacher_class.append(class_obj)
            self.session.commit()
            print("\033[32;1m班级创建成功\033[0m")
        else:
            print("\33[31;1m系统错误：班级已经存在\33[0m")

    def add_student(self):
        '''
        添加学生
        :return:
        '''
        class_input = input("\033[33;0m请输入要添加学员的班级名:\033[0m").capitalize()
        class_obj = self.session.query(Class).filter(Class.class_name == class_input).first()
        if class_obj and class_obj.teacher_keys[0] == self.teacher_obj:
            stu_input = input("\033[33;0m请输入要添加的学员名:\033[0m").capitalize()
            stu_obj = self.session.query(Student).filter(Student.stu_name == stu_input).first()
            if stu_obj is None:
                QQ_input = input("\033[33;0m请输入要添加的学员QQ:\033[0m").capitalize()
                if QQ_input.isdigit():
                    QQ_input = int(QQ_input)
                    stu_qq_obj = self.session.query(Student).filter(Student.QQ == QQ_input).first()
                    if stu_qq_obj is None:
                        stu_obj = Student(stu_name = stu_input,QQ = QQ_input)
                        class_obj.class_student.append(stu_obj)
                        self.session.add(stu_obj)
                        self.session.commit()
                        print('\033[32;1m学员添加成功\033[0m')
                    else:
                        print('\033[31;1mQQ号已存在\033[0m')
                else:
                    print('\033[31;1mQQ号必须是数子\033[0m')
            else:
                print("\33[31;1m系统错误：学员已经存在\33[0m")
        else:
            print("\33[31;1m输入错误：班级不存在或没有权限管理此班级\33[0m")

    def add_lesson(self):
        '''
        添加课程节次
        :return:
        '''
        class_input = input("\033[33;0m请输入要添加节次的班级名:\033[0m").capitalize()
        class_obj = self.session.query(Class).filter(Class.class_name == class_input).first()
        if class_obj and class_obj.teacher_keys[0] == self.teacher_obj:
            lesson_input = input("\033[33;0m请输入添加的lesson名（类day1）:\033[0m")
            lesson_obj = self.session.query(Lesson).filter(Lesson.lesson_name == lesson_input).first()
            if lesson_obj is None:      #所需添加的lesson名不存在可创建
                lesson_obj = Lesson(lesson_name = lesson_input)
                self.session.add(lesson_obj)
                self.session.commit()
                print('\033[32;1mlesson表数据创建成功\033[0m')

                #在class_m2m_lesson创建一条关联数据
                rest = (self.session.query(class_m2m_lesson).filter(class_m2m_lesson.class_id == class_obj.class_id).
                     filter(class_m2m_lesson.lesson_id == lesson_obj.lesson_id)).first()
                if rest is None:
                    rest = class_m2m_lesson(class_id = class_obj.class_id,lesson_id = lesson_obj.lesson_id)
                    self.session.add(rest)
                    self.session.commit()
                    print('\033[32;1m class_m2m_lesson表数据创建成功\033[0m')
            else:
                print("\33[31;1m系统错误：课节已经存在\33[0m")
        else:
            print("\33[31;1m输入错误：班级不存在或没有权限管理此班级\33[0m")


    def add_study_record(self):
        '''
        添加上课记录数据
        :return:
        '''
        class_input = input("\033[33;0m请输入要添加记录的班级名:\033[0m").capitalize()
        class_obj = self.session.query(Class).filter(Class.class_name == class_input).first()
        if class_obj and class_obj.teacher_keys[0] == self.teacher_obj:
            lesson_input = input("\033[33;0m请输入添加记录的lesson名（类day1）:\033[0m")
            lesson_obj = self.session.query(Lesson).filter(Lesson.lesson_name == lesson_input).first()
            if lesson_obj is not None:                      #课节已存在
                class_lesson_obj = self.session.query(class_m2m_lesson).\
                    filter(class_m2m_lesson.class_id == class_obj.class_id).\
                    filter(class_m2m_lesson.lesson_id == lesson_obj.lesson_id).first()
                if class_lesson_obj is not None:
                    study_record_obj = self.session.query(Study_record).\
                        filter(Study_record.class_m2m_lesson_id == class_lesson_obj.id).first()
                    if study_record_obj is None:
                        for student in class_obj.class_student:    #循环遍历学生是否已在上课记录表中已记录
                            stu_id_obj = self.session.query(Study_record).\
                                filter(Study_record.stu_id == student.stu_id).first()
                            if stu_id_obj is None:          #打印未在有上课记录的学生信息
                                print('\033[32;1m未有上课记录的学生信息:\033[0m',student)
                                status_input = input("输入%s 的上课状态（Y/N）：" % student.stu_name).capitalize()
                                if status_input != 'N': status_input = 'Y'
                                while True:
                                    score_input = input("输入 %s 的成绩："
                                                        % student.stu_name).capitalize()
                                    if score_input.isdigit():
                                        score_input = int(score_input)
                                        if score_input >=0 and  score_input <=100:
                                            study_record_new = Study_record(
                                                class_m2m_lesson_id = class_lesson_obj.id,
                                                stu_id = student.stu_id,
                                                status = status_input,
                                                score = score_input
                                            )
                                            self.session.add(study_record_new)
                                            self.session.commit()
                                            print('\033[32;1m上课记录添加完成\033[0m')
                                            break
                                        else:
                                            print('\033[31;1m请输入成绩超出有效范围\033[0m')
                                    else:
                                        print('\033[31;1m请输入有效成绩\033[0m')
                    else:
                        print("\33[31;1m系统错误：上课记录已经存在\33[0m")
                else:
                    print("\33[31;1m系统错误：class_m2m_lesson表中无记录\33[0m")
            else:
                print("\33[31;1m系统错误：课节不存在\33[0m")
        else:
            print("\33[31;1m输入错误：班级不存在或没有权限管理此班级\33[0m")


    def modify_scores(self):
        '''
        修改学生成绩函数
        :return:
        '''
        class_input = input("\033[33;0m请输入要添加记录的班级名:\033[0m").capitalize()
        class_obj = self.session.query(Class).filter(Class.class_name == class_input).first()
        if class_obj and class_obj.teacher_keys[0] == self.teacher_obj:
            lesson_input = input("\033[33;0m请输入添加记录的lesson名（类day1）:\033[0m")
            lesson_obj = self.session.query(Lesson).filter(Lesson.lesson_name == lesson_input).first()
            if lesson_obj is not None:  # 课节已存在
                class_lesson_obj = self.session.query(class_m2m_lesson). \
                    filter(class_m2m_lesson.class_id == class_obj.class_id). \
                    filter(class_m2m_lesson.lesson_id == lesson_obj.lesson_id).first()
                if class_lesson_obj is not None:    #判断该课节在class_m2m_lesson表是否存在
                    study_record_obj = self.session.query(Study_record). \
                        filter(Study_record.class_m2m_lesson_id == class_lesson_obj.id).first()
                    if study_record_obj is not None:
                        while True:
                            print('\033[32;1m已有上级记录的学生信息\033[0m')
                            for student in class_obj.class_student:  # 循环遍历学生是否已在上课记录表中已记录
                                stu_id_obj = self.session.query(Study_record). \
                                    filter(Study_record.stu_id == student.stu_id).first()
                                if stu_id_obj is not None:  # 打印未在有上课记录的学生信息
                                    print('\033[32;1m学生名:【%s】  Status：【%s】   '
                                          '成绩：【%s】\033[0m'
                                          %(student.stu_name,stu_id_obj.status,stu_id_obj.score))
                            stu_input = input("\033[33;0m请输入要修改记录的学生名[Q 退出]:\033[0m").capitalize()
                            if stu_input == 'Q':break
                            # 判断输入的学生名是否存在
                            stu_obj = self.session.query(Student).filter(Student.stu_name == stu_input).first()
                            if stu_obj is not None:
                                #判断该学生在Study_record表中有记录
                                study_stu_obj = self.session.query(Study_record).\
                                    filter(Study_record.stu_id == stu_obj.stu_id).first()
                                if study_stu_obj is not None:       #该学生已有上课记录
                                    status_input = input("修改%s 的上课状态（Y/N）：" % stu_obj.stu_name).capitalize()
                                    if status_input != 'Y': status_input = 'N'
                                    while True:
                                        score_input = input("修改 %s 的成绩："
                                                            % stu_obj.stu_name).capitalize()
                                        if score_input.isdigit():
                                            score_input = int(score_input)
                                            if score_input >= 0 and score_input <= 100:
                                                study_stu_obj.status = status_input
                                                study_stu_obj.score = score_input
                                                self.session.commit()
                                                print('\033[32;1m记录修改完成\033[0m')
                                                break
                                            else:
                                                print('\033[31;1m请输入成绩超出有效范围\033[0m')
                                        else:
                                            print('\033[31;1m请输入有效成绩\033[0m')
                                else:
                                    print("\33[31;1m系统错误：该学生上课记录未存在\33[0m")
                            else:
                                print("\33[31;1m系统错误：该学生未存在\33[0m")
                    else:
                        print("\33[31;1m系统错误：上课记录未存在\33[0m")
                else:
                    print("\33[31;1m系统错误：class_m2m_lesson表中无记录\33[0m")
            else:
                print("\33[31;1m系统错误：课节不存在\33[0m")
        else:
            print("\33[31;1m输入错误：班级不存在或没有权限管理此班级\33[0m")

    def exit(self):
        exit('\033[31;0m感谢使用管理系统,\033[0m')

