#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
try:
    code            #语句体
except (error1,error2....) as e:    #抓住多个错误   e:打印错误内容
    print(e)
except Exception as e:  #抓主所有错误，不建议一开始用
finally:    #不管有没有错都执行
'''
class Dog(object):
    def __init__(self,name):
        self.name =name

    def eat(self, food):
        print("%s is eat %s" % (self.name, food))

d = Dog("Chenronghua")
choise = input(">>>:").strip()
try:
    data = {}
    data
    getattr(d,choise)
    a = 1
    print(a)
except AttributeError as e :
    print(e)
# finally:
#     print("不管有没有错都执行")
except Exception as e:
    print("未知错误:%s"%e)

