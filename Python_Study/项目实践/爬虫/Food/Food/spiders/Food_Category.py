# -*- coding:utf-8 -*-
# Author:D.Gray
import scrapy,json
from scrapy import Request
from sqlalchemy.orm import sessionmaker
from Food import models
class FoodScrapySpider(scrapy.Spider):
    name = "food_category"
    start_urls = ["http://food.boohee.com/fb/v1/categories/list"]

    def parse(self,response):
        d = json.loads(response.text)
        group_list = d["group"][0]["categories"]
        print("类目信息".decode("utf-8".center(50,"-")))
        for item in group_list:
            category_id = item["id"]
            name = item["name"]
            img_url = item["image_url"]
            print("%s %s\n %s"%(category_id,name,img_url))
            # print("添加数据".decode("utf-8").center(50,"+"))
            # Session_class = sessionmaker(bind=models.engine)
            # session = Session_class()
            # obj = models.Food_Category(category_id=category_id,name=name,img_url=img_url)
            # session.add(obj)
            # session.commit()
            # print("数据添加成功".decode("utf-8"))


