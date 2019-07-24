# -*- coding:utf-8 -*-
# Author:D.Gray
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import func

engine = sqlalchemy.create_engine('mysql+pymysql://root:admin1988@localhost/oldboy',encoding = 'utf-8')

Base = declarative_base()
class User(Base):
    __tablename__ = 'user.txt'
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    password = Column(String(64),nullable=False)

    def __repr__(self):
        return '<%s name:%s>'%(self.id,self.name)

Base.metadata.create_all(engine)
print('创建表成功')

class Student(Base):
    '''
    映射一个库中已存在的表,可直接对其插入数据
    '''
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    age = Column(Integer,nullable=False)
    register_date = Column(String(64),nullable=False)
    sex = Column(String(32),nullable=False)

    def __repr__(self):
        return '<%s name:%s>'%(self.id,self.name)
Base.metadata.create_all(engine)
print('创建表成功')

class Study_record(Base):
    '''
    映射一个库中已存在的表,可直接对其插入数据
    '''
    __tablename__ = 'study_record'
    id = Column(Integer,primary_key=True)
    day = Column(Integer,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey('student.id'))
    student = relationship('Student',backref = 'study_key')
    def __repr__(self):
        return '<%s  day:%s  status:%s>'%(self.student.name,self.day,self.status)
Base.metadata.create_all(engine)
print('创建表成功')

Session_class = sessionmaker(bind=engine)
session = Session_class()

# user_obj = Student(name = 's1',age = 34,register_date = '2017-09-08',sex = 'N')
# session.add(user_obj)
# session.commit()
# print('数据插入成功')

print('连表查询语法一:'.center(50,'-'))
print(session.query(User,Student).filter(User.id == Student.id).all())

print('连表查询语法二:'.center(50,'-'))
print(session.query(Study_record).join(Student).all())   #这种写法必须两表之间有外键关联
