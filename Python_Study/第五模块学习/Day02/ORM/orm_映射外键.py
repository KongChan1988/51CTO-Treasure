# -*- coding:utf-8 -*-
# Author:D.Gray
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import func

engine = create_engine('mysql+pymysql://root:admin1988@localhost/18girls',encoding = 'utf-8')

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    register_date = Column(String(32),nullable=False)
    sex = Column(String(32),nullable=False,default='N')

    def __repr__(self):
        return '<%s name:%s>'%(self.id,self.name)
Base.metadata.create_all(engine)
print('创建表成功')

class StudyRecord(Base):
    from sqlalchemy import Column, String, Integer, ForeignKey
    from sqlalchemy.orm import sessionmaker, relationship
    __tablename__ = 'study_record'
    id = Column(Integer,primary_key=True)
    day = Column(Integer)
    status = Column(String(32),nullable=False,default='Y')
    stu_id = Column(Integer,ForeignKey('student.id'))   #ForeignKey(所需关联表名.字段名)

    # study_record表通过students查询Student类中也就是student表中数据，
    # 同时student表也可以通过my_study_record反查StudyRecord类中所有数据
    students = relationship('Student',backref = 'my_study_record')
    def __repr__(self):
        return '<%s  day:%s  status:%s>'%(self.students.name,self.day,self.status)
Base.metadata.create_all(engine)
print('创建表成功')

Session_class = sessionmaker(bind=engine)
session = Session_class()

# s1 = Student(name = 'Alex',register_date = '2015-08-05')
# s2 = Student(name = 'Jack',register_date = '2016-07-02')
# s3 = Student(name = 'Mary',register_date = '2016-05-05')
# s4 = Student(name = 'Kyo',register_date = '2015-06-05')
#
# sd1= StudyRecord(day = 1,stu_id = 1)
# sd2= StudyRecord(day = 2,stu_id = 1)
# sd3= StudyRecord(day = 3,stu_id = 1)
# sd4= StudyRecord(day = 1,status = 'N',stu_id = 2)
# sd5= StudyRecord(day = 4,status = 'N',stu_id = 1)
#
# session.add_all([s1,s2,s3,s4,sd1,sd2,sd3,sd4,sd5])
# session.commit()
# print('数据添加完成')

print('查询'.center(50,'-'))
stu_obj = session.query(Student).filter(Student.name == 'Alex').all()
print(stu_obj)

print('连表查询'.center(50,'-'))
study_obj = session.query(Student).filter(Student.name == 'Alex').join(StudyRecord).all()
print(study_obj)

print('外键查询'.center(50,'-'))  #查询Alex上课情况
ForeignKey_obj = session.query(Student).filter(Student.name == 'alex').first()
print(ForeignKey_obj.my_study_record)