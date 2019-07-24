# -*- coding:utf-8 -*-
# Author:D.Gray
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:admin1988@localhost/oldboy?charset=utf8')

Base = declarative_base()
class User(Base):
    __tablename__ = 'user.txt'
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    password = Column(String(64),nullable=False)

Base.metadata.create_all(engine)
print('创建表成功')

print('插入数据'.center(50,'-'))
Session_class = sessionmaker(bind=engine)    #创建与数据库绘画session_class,这里返回的是个类 不是实例
session = Session_class()   #生成session实例

user_obj1 = User(name = 'mary',password = 'alex7143')  #生成实例对象
user_obj2 = User(name = 'jack',password = 'jack123')

session.add(user_obj1)  #此时创建数据对象并添加到这个session里
session.add(user_obj2)

print(user_obj1.name,user_obj2.name)
session.commit()     #现在才统一提交，创建数据
print('数据添加成功')

