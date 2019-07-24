# -*- coding:utf-8 -*-
# Author:D.Gray
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,String,Integer,ForeignKey,Table
from conf.setting import engine

Base = declarative_base()

teacher_m2m_class = Table(
    'teacher_m2m_class',Base.metadata,
    Column('teacher_id',Integer,ForeignKey('teacher.teacher_id')),
    Column('class_id',Integer,ForeignKey('class.class_id'))
)

class_m2m_student = Table(
    'class_m2m_student',Base.metadata,
    Column('class_id',Integer,ForeignKey('class.class_id')),
    Column('student_id',Integer,ForeignKey('student.stu_id'))
)

class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer,primary_key=True)
    teacher_name = Column(String(64),nullable=False)
    teacher_class = relationship('Class',secondary = teacher_m2m_class,backref = 'teacher_keys')

    def __repr__(self):
        return '讲师:【%s】'%(self.teacher_name)

class Class(Base):
    __tablename__ = 'class'
    class_id = Column(Integer,primary_key=True)
    class_name = Column(String(64),nullable=False)
    course = Column(String(64),nullable=False)
    class_student = relationship('Student',secondary = class_m2m_student,backref = 'class_keys')
    def __repr__(self):
        return '班级:【%s】'%(self.class_name)

class Student(Base):
    __tablename__ = 'student'
    stu_id = Column(Integer,primary_key=True)
    stu_name = Column(String(64),nullable=False)
    QQ = Column(String(64),nullable=False,unique=True)

    def __repr__(self):
        return '学生名：【%s】'%self.stu_name

class Lesson(Base):
    __tablename__ = 'lesson'
    lesson_id = Column(Integer,primary_key=True)
    lesson_name = Column(String(64),nullable=False)
    def __repr__(self):
        return '课节名【%s】'%(self.lesson_name)

class Study_record(Base):
    __tablename__ = 'study_record'
    id = Column(Integer,primary_key=True)
    class_m2m_lesson_id = Column(Integer,ForeignKey('class_m2m_lesson.id'),nullable=False)
    stu_id = Column(Integer,ForeignKey('student.stu_id'),nullable=False)
    status = Column(String(64),nullable=False,default='Y')
    score = Column(Integer,nullable=False)
    class_m2m_lesson = relationship('class_m2m_lesson',backref = 'study_keys')
    students = relationship('Student',backref = 'study_student_keys')

    def __repr__(self):
        return "\033[35;0m%s,%s,状态：【%s】,成绩：【%s】\33[0m" % (
        self.class_m2m_lessons, self.students, self.status, self.score)


class class_m2m_lesson(Base):
    __tablename__ = 'class_m2m_lesson'
    id = Column(Integer,primary_key=True)
    class_id = Column(Integer,ForeignKey('class.class_id'))
    lesson_id = Column(Integer,ForeignKey('lesson.lesson_id'))
    class_lesson = relationship('Class',backref = 'class_m2m_lesson')
    lesson_class = relationship('Lesson',backref = 'lesson_m2m_class')

    def __repr__(self):
        return '班级信息：【%s】    课节信息：【%s】'%(self.class_lesson,self.lesson_class)

Base.metadata.create_all(engine)
print('创建表成功')