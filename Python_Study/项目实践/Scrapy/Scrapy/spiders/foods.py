# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
from Scrapy.spiders import models
from sqlalchemy.orm import sessionmaker
class FoodsSpider(scrapy.Spider):
    name = 'foods'
    allowed_domains = ['http://food.boohee.com/fb/v1/categories/list']
    start_urls = ['http://food.boohee.com/fb/v1/categories/list']

    def start_requests(self):
        '''
        食物分类 value为变量 （1-主食类 2-肉蛋类  3-大豆及制品）  总共12大分类
        :return:
        '''
        for i in range(1,13):
            for p in range(1,11):
                new_url = "http://food.boohee.com/fb/v1/foods?kind=group&value=%s&order_by=1&page=%s&order_asc=0"%(i,p)
                yield Request(url=new_url,callback=self.check)

    def check(self,response):
        d = response.text
        food = json.loads(d)
        for item in food["foods"]:
            print("食物信息".center(50, "-"))
            # print(item)
            self.food_id = item["id"]
            self.food_name = item["name"]
            self.food_code = item["code"]
            thumb_image_url = item["thumb_image_url"]
            calory = item["calory"]
            protein = item["protein"]
            fat = item["fat"]
            carbohydrate = item["carbohydrate"]
            fiber_dietary = item["fiber_dietary"]
            vitamin_a = item["vitamin_a"]
            vitamin_c = item["vitamin_c"]
            vitamin_e = item["vitamin_e"]
            # carotene = item["carotene"]   胡萝卜素
            thiamine = item["thiamine"]
            lactoflavin = item["lactoflavin"]
            niacin = item["niacin"]
            cholesterol = item["cholesterol"]
            magnesium = item["magnesium"]
            calcium = item["calcium"]
            iron = item["iron"]
            zinc = item["zinc"]
            copper = item["copper"]
            manganese = item["manganese"]
            kalium = item["kalium"]
            # phosphor = item["phosphor"]   磷
            natrium = item["natrium"]
            selenium = item["selenium"]
            print(self.food_id,self.food_name,self.food_code)
            food_url = "http://food.boohee.com/fb/v1/foods/%s/mode_show"%(self.food_code)
            print(food_url)
            print("食物营养数据".center(30, "-"))
            print("calory(卡路里)：%s\n fiber_dietary(膳食纤维)：%s\n protein(蛋白质)：%s\n fat(脂肪)：%s\n "
                  "carbohydrate(碳水化合物)：%s\n vitamin_a(维他命A)：%s\n vitamin_c(维他命C)：%s\n"
                  "vitamin_e(维他命E)：%s\n thiamine(硫胺素)：%s\n lactoflavin(核黄素)：%s\n"
                  "niacin(烟酸)：%s\n magnesium(镁)：%s\n calcium(钙)：%s\n iron(铁)：%s\n "
                  "zinc(锌)：%s\n copper(铜)：%s\n manganese(锰)：%s\n kalium(钾)：%s\n "
                  "natrium(钠)：%s\n selenium(硒)：%s\n cholesterol(胆固醇)：%s\n "
                  %(calory,fiber_dietary,protein,fat,carbohydrate,vitamin_a,vitamin_c,vitamin_e,thiamine,
                    lactoflavin,niacin,magnesium,calcium,iron,zinc,copper,manganese,kalium,natrium,selenium,
                    cholesterol)
                  )
            # for k,v in item.items():
            #     print("%s : %s"%(k,v))
            # print("插入数据\n")
            # Session_Food = sessionmaker(bind=models.engine)
            # session = Session_Food()
            # obj = models.Food(id=self.food_id, name=self.food_name, code=self.food_code, thumb_image_url=thumb_image_url,
            #                   calory=int(eval(calory)*100),fiber_dietary=int(eval(fiber_dietary)*100),
            #                   protein=int(eval(protein)*100),
            #                   fat=int(eval(fat)*100),carbohydrate=int(eval(carbohydrate)*100),
            #                   vitamin_a=int(eval(vitamin_a)*100),vitamin_c=int(eval(vitamin_c)*100),
            #                   vitamin_e=int(eval(vitamin_e)*100),
            #                   thiamine=int(eval(thiamine)*100),lactoflavin=int(eval(lactoflavin)*100),
            #                   niacin=int(eval(niacin)*100),
            #                   magnesium=int(eval(magnesium)*100),calcium=int(eval(calcium)*100),
            #                   iron=int(eval(iron)*100),
            #                   zinc=int(eval(zinc)*100),
            #                   copper=int(eval(copper)*100),manganese=int(eval(manganese)*100),
            #                   kalium=int(eval(kalium)*100),
            #                   natrium=int(eval(natrium)*100),selenium=int(eval(selenium)*100),
            #                   cholesterol=int(eval(cholesterol)*100)
            #                   )
            # obj = models.Food(id=self.food_id, name=self.food_name, code=self.food_code,
            #                   thumb_image_url=thumb_image_url,
            #                   calory=int(eval(calory)*100), fiber_dietary=int(eval(fiber_dietary)*100),
            #                   protein=int(eval(protein)*100),
            #                   fat=int(eval(fat)*100), carbohydrate=int(eval(carbohydrate)*100),
            #                   vitamin_a=vitamin_a, vitamin_c=vitamin_c,
            #                   vitamin_e=vitamin_e,
            #                   thiamine=thiamine, lactoflavin=lactoflavin,
            #                   niacin=niacin,
            #                   magnesium=magnesium, calcium=calcium,
            #                   iron=iron,
            #                   zinc=zinc,
            #                   copper=copper, manganese=manganese,
            #                   kalium=kalium,
            #                   natrium=natrium, selenium=selenium,
            #                   cholesterol=cholesterol
            #                   )
            # print(obj.protein,obj.kalium)
            # session.add(obj)
            # session.commit()
            # print("数据添加成功")
            # with open("E:\\python_work\\51CTO_Python\项目实践\Scrapy\Scrapy\spiders\\test.json","a",encoding="utf-8") as f:
            #     f.write(json.dumps(item,indent=4))
            #     # f.write(item)           将数据写入test.json文件中

    def parse(self, response):
        pass

