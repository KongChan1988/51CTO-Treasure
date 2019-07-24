#-*- Coding:utf-8 -*-
# Author: D.Gray

class SchoolMember(object):
    member = 0
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.ennorl()

    def ennorl(self):
        print('%s实例化注册了'%self.name)
        SchoolMember.member +=1

    def __del__(self):
        print('开除了%s'%self.name)
        SchoolMember.member -= 1

    def info(self):
        for k,v in self.__dict__.items():
            print('%s:%s'%(k,v))


class Teacher(SchoolMember):
    def __init__(self,name,addr,age,salary,course):
        SchoolMember.__init__(self,name,addr)
        self.age = age
        self.salary = salary
        self.course = course

    def teachering(self):
        print('%s教%s语言'%(self.name,self.course))

t1 = Teacher('alex','中春路',30,50000,'Python')
print(SchoolMember.member)
print(t1.info())



