# -*- coding: utf-8 -*-
import scrapy,json
from scrapy import Request
from sqlalchemy.orm import sessionmaker
from Food import models
class FoodScrapySpider(scrapy.Spider):
    name = "food"

    def __init__(self):
        '''
        value：分类  1-主食类  2-肉蛋类  3-大豆及制品类....总共12大分类  12-其他分类时候没有target_name 要去掉
        page：分页 总共可分10页
        '''
        self.start_urls=[]
        for i in range(1,13):
            for p in range(1,11):
                url = "http://food.boohee.com/fb/v1/foods?kind=group&value=%s&order_by=1&page=%s&order_asc=0"%(i,p)
                self.start_urls.append(url)

    def parse(self,response):
        '''
        获取url = "http://food.boohee.com/fb/v1/foods?kind=group&value=%s&order_by=1&page=%s&order_asc=0"%(i,p)接口
        数据中的各商品codde值 并做字符串拼接对self.food_url = "http://food.boohee.com/fb/v1/foods/%s/mode_show"%self.code
        商品详情接口发送请求
        :param response:
        :return:
        '''
        d = json.loads(response.text)
        a = response.url.split("&")[1]
        group_id = a.split("=")[1]         #["value","1"]
        for item in d["foods"]:
            self.code = item["code"]
            self.food_url = "http://food.boohee.com/fb/v1/foods/%s/mode_show"%self.code
            yield Request(url=self.food_url,callback=self.check,meta={"group_id":group_id})

    def check(self,response):
        '''
        获取商品详情接口数据参数
        :param response:
        :return:
        '''
        d = json.loads(response.text)
        id = d["id"]
        name = d["name"]
        code = d["code"]
        image_url = d["thumb_image_url"]
        group_id = response.meta.get("group_id")
        # target_name = d["compare"]["target_name"]
        appraise = d["appraise"]
        food_url = "http://food.boohee.com/fb/v1/foods/%s/mode_show"%code
        print "食物信息".decode("utf-8").center(50,"-")
        print "group_id:", group_id
        print "%s %s %s \n%s\n%s\n%s\n" %(id,name,code,appraise,food_url,image_url)
        # print "食物营养数据".decode("utf-8").center(30, "=")
        calory = d["ingredient"]["calory"]
        protein = d["ingredient"]["protein"]
        fat = d["ingredient"]["fat"]
        carbohydrate = d["ingredient"]["carbohydrate"]
        fiber_dietary = d["ingredient"]["fiber_dietary"]
        vitamin_a = d["ingredient"]["vitamin_a"]
        vitamin_c = d["ingredient"]["vitamin_c"]
        vitamin_e = d["ingredient"]["vitamin_e"]
        carotene = d["ingredient"]["carotene"]
        thiamine = d["ingredient"]["thiamine"]
        lactoflavin = d["ingredient"]["lactoflavin"]
        niacin = d["ingredient"]["niacin"]
        cholesterol = d["ingredient"]["cholesterol"]
        magnesium = d["ingredient"]["magnesium"]
        calcium = d["ingredient"]["calcium"]
        iron = d["ingredient"]["iron"]
        zinc = d["ingredient"]["zinc"]
        copper = d["ingredient"]["copper"]
        manganese = d["ingredient"]["manganese"]
        kalium = d["ingredient"]["kalium"]
        phosphor = d["ingredient"]["phosphor"]
        natrium = d["ingredient"]["natrium"]
        selenium = d["ingredient"]["selenium"]
        gi = d["gi"]
        gl = d["gl"]

        # print "calory(卡路里):{0}\nprotein(蛋白质):{1}\nfat(脂肪):{2}\ncarbohydrate(碳水化合物):{3}\nfiber_dietary(膳食纤维):{4}\n" \
        #       "vitamin_a(vitamin_a):{5}\nvitamin_c(vitamin_c):{6}\nvitamin_e(vitamin_e):{7}\ncarotene(胡萝卜素):{8}\n" \
        #       "thiamine(硫胺素):{9}\nlactoflavin(核黄素):{10}\nniacin(钠):{11}\ncholesterol(胆固醇):{12}\nmagnesium(镁):{13}\n" \
        #       "calcium(钙):{14}\niron(铁):{15}\nzinc(锌):{16}\ncopper(铜):{17}\nmanganese(锰):{18}\nkalium(钾):{19}\nphosphor(磷):{20}\n" \
        #       "natrium(钠):{21}\nselenium(硒):{22}\n".decode("utf-8").format(calory,protein,fat,carbohydrate,fiber_dietary,vitamin_a,vitamin_c,
        #                                          vitamin_e,carotene,thiamine,lactoflavin,niacin,cholesterol,magnesium,
        #                                         calcium,iron,zinc,copper,manganese,kalium,phosphor,natrium,selenium)
        print "数据导入".decode("utf-8").center(50,"+")
        Session_class = sessionmaker(bind=models.engine)
        session = Session_class()
        obj1 = models.Food(id=id,name=name,code=code,image_url=image_url,food_url=food_url,
                                    appraise=appraise)
        obj2 = models.Food_Nutrition(id=id,name=name,code=code,calory=calory,protein=protein,fat=fat,carbohydrate=carbohydrate,
                           fiber_dietary=fiber_dietary,vitamin_a=vitamin_a,vitamin_c=vitamin_c,vitamin_e=vitamin_e,
                           carotene=carotene,thiamine=thiamine,lactoflavin=lactoflavin,niacin=niacin,cholesterol=cholesterol,
                           magnesium=magnesium,calcium=calcium,iron=iron,zinc=zinc,copper=copper,manganese=manganese,
                           kalium=kalium,phosphor=phosphor,natrium=natrium,selenium=selenium,gi=gi,gl=gl,category_id=group_id)

        session.add_all([obj1,obj2])
        session.commit()
        print "数据添加成功".decode("utf-8")

        # for k,v in d["ingredient"].items():
        #     print k,v


