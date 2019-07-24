#-*-coding:utf-8 -*-
# Author: D.Gray
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Float,String,Integer,ForeignKey
from sqlalchemy.orm import relationship,sessionmaker
engine = create_engine("mysql+pymysql://root:root@localhost/foodscripy?charset=utf8")
Base = declarative_base()
class Food_Category(Base):
    __tablename__ = "Food_Category"
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    img_url = Column(String(64))
    category_id = Column(Integer)

class Food(Base):
    __tablename__ = "Food"
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    code = Column(String(64))
    image_url = Column(String(64))
    food_url = Column(String(64))
    # target_name = Column(String(32))
    appraise = Column(String(128))

class Food_Nutrition(Base):
    __tablename__ = "Food_Nutrition"
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    code = Column(String(64))
    calory = Column(Float)
    protein = Column(Float)
    fat = Column(Float)
    carbohydrate = Column(Float)
    fiber_dietary = Column(Float)
    vitamin_a = Column(Float)
    vitamin_c = Column(Float)
    vitamin_e = Column(Float)
    carotene = Column(Float)
    thiamine = Column(Float)
    lactoflavin = Column(Float)
    niacin = Column(Float)
    cholesterol = Column(Float)
    magnesium = Column(Float)
    calcium = Column(Float)
    iron = Column(Float)
    zinc = Column(Float)
    copper = Column(Float)
    manganese = Column(Float)
    kalium = Column(Float)
    phosphor = Column(Float)
    natrium = Column(Float)
    selenium = Column(Float)
    gi = Column(Float)
    gl = Column(Float)
    category_id = Column(Integer,ForeignKey("Food_Category.category_id"))
    food_category= relationship("Food_Category",backref="food_record")

# Base.metadata.create_all(engine)
# print "表创建成功"
Session_class = sessionmaker(bind=engine)
session = Session_class()
food_obj = session.query(Food_Nutrition).filter(Food_Nutrition.id == 86134).first()
print(food_obj.food_category.name)




