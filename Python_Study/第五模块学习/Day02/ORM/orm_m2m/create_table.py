# -*- coding:utf-8 -*-
# Author:D.Gray
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import Column,String,Integer,ForeignKey,Table

engine = create_engine('mysql+pymysql://root:admin1988@localhost/18girls?charset=utf8')
Base = declarative_base()

book_m2m_author = Table(
    'book_m2m_author',Base.metadata,
    Column('author_id',ForeignKey('author.id'),nullable=False),
    Column('book_id',ForeignKey('book.id'),nullable=False)
)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),nullable=False)
    pub_date = Column(String(64),nullable=False)
    authors = relationship('Author',secondary = book_m2m_author,backref = 'books_key')
    def __repr__(self):
        return '<%s>'%self.name

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),nullable=False)

    def __repr__(self):
        return self.name

Base.metadata.create_all(engine)
print('创建表成功')