# -*- coding:utf-8 -*-
# Author:D.Gray
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

engine = sqlalchemy.create_engine('mysql+pymysql://root:admin1988@localhost/oldboy?charset=utf8')

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

print('查询'.center(50,'-'))
Session_class = sessionmaker(bind=engine)
session = Session_class()
data = session.query(User).filter(User.name=='jay').all()
data1 = session.query(User).filter(User.name=='jay').first()
data2 = session.query(User).filter(User.id>2).filter(User.id<4).all()
print(data)

print('修改'.center(50,'-'))
Session_class = sessionmaker(bind=engine)
session = Session_class()
data = session.query(User).filter(User.id>2).filter(User.id<4).all()
data.name = 'alex'
data.password = 'root'
session.commit()  #修改数据时必须要 commit()下
print(data)

print('统计'.center(50,'-'))
Session_class = sessionmaker(bind=engine)
session = Session_class()
data = session.query(User).filter(User.name.in_(['alex','jay'])).count()
print(data)

print('分组统计'.center(50,'-'))
from sqlalchemy import func
Session_class = sessionmaker(bind=engine)
session = Session_class()
data = session.query(User.name,func.count(User.name)).group_by(User.name).all()
print(data)


print('排序'.center(50,'-'))
Session_class = sessionmaker(bind=engine)
session = Session_class()
data = session.query(User).order_by(User.id.desc()).all()
print(data)


print('回滚'.center(50,'-'))
user_obj = User(name = 'jay',password = 'jay123')
session.add(user_obj)
print('回滚前：',session.query(User).filter(User.name.in_(['alex','jay'])).all())
session.rollback()
print('回滚后：',session.query(User).filter(User.name.in_(['alex','jay'])).all())
session.commit()


print('删除'.center(50,'-'))
data = session.query(User).filter(User.name=='jay').delete()
print(data)

