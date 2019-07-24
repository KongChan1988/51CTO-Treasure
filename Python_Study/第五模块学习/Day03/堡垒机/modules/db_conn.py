#-*-coding:utf-8 -*-
# Author: D.Gray
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf import setting

engine = create_engine(setting.CONN)
# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
SessionCls = sessionmaker(bind=engine)
session = SessionCls()