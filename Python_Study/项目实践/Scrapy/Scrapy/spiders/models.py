# -*- coding:utf-8 -*-
# Author:D.Gray
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:root@localhost/foodscripy?charset=utf8")
Base = declarative_base()
class Food(Base):
    __tablename__ = "Food"
    id = Column(Integer,primary_key=True)
    name = Column(String(64),nullable=False)
    code = Column(String(64),nullable=False)
    thumb_image_url = Column(String(64),nullable=False)
    calory = Column(Integer)
    protein = Column(Integer)
    fat = Column(Integer)
    carbohydrate = Column(Integer)
    fiber_dietary = Column(Integer)
    vitamin_a = Column(Integer)
    vitamin_c = Column(Integer)
    vitamin_e = Column(Integer)
    thiamine = Column(Integer)
    lactoflavin = Column(Integer)
    niacin = Column(Integer)
    cholesterol = Column(Integer)
    magnesium = Column(Integer)
    calcium = Column(Integer)
    iron = Column(Integer)
    zinc = Column(Integer)
    copper = Column(Integer)
    manganese = Column(Integer)
    kalium = Column(Integer)
    natrium = Column(Integer)
    selenium = Column(Integer)

Base.metadata.create_all(engine)
print("表创建成功")


