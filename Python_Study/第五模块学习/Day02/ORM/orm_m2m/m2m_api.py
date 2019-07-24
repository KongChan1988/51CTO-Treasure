# -*- coding:utf-8 -*-
# Author:D.Gray
import sqlalchemy
from Day02.ORM.orm_m2m import create_table
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=create_table.engine)
session = Session_class()

# b1 = create_table.Book(name = '跟Alex学Python',pub_date = '2016-07-08')
# b2 = create_table.Book(name = '失控',pub_date = '2015-02-08')
# b3 = create_table.Book(name = '三重门',pub_date = '2017-05-08')
#
# a1 = create_table.Author(name = 'Alex')
# a2 = create_table.Author(name = 'Jack')
# a3 = create_table.Author(name = 'Mary')
# b1.authors = [a1,a2]
# b2.authors = [a2]
# b3.authors = [a1,a2,a3]
#
# session.add_all([a1,a2,a3,b1,b2,b3])
# session.commit()
# print('数据添加完成')

print('多对多查询'.center(50,'-'))
#根据作者名查所对应的书
author_data = session.query(create_table.Author).filter(create_table.Author.name == 'alex').first()
print(author_data.name,author_data.books_key)
#根据书名查作者
book_data = session.query(create_table.Book).filter(create_table.Book.id == 3).first()
print(book_data.name,book_data.authors)

# print('删除'.center(50,'-'))
# book_data.authors.remove(author_data)
# session.commit()
# print('删除后结果:',book_data.name,book_data.authors)