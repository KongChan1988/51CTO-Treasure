# -*- coding:utf-8 -*-
# Author:D.Gray

class SchoolMember(object):
    '''
    学校成员父类
    '''
    member = 0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        '''注册'''
        print('Just enrolled a New school member [%s] ' % self.name)
        SchoolMember.member += 1

    def tell(self):
        '''打印个人信息'''
        print('''%s info'''.center(50,'-')%self.name)
        for k,v in self.__dict__.items():
            print('\t%s:%s'%(k,v))
        print('''end'''.center(50,'-'))

    def __del__(self):
        print('开除了 %s...'%self.name)
        SchoolMember.member -= 1

class School(object):
    '''学校类'''
    def oprn_branch(self,addr):
        print('多继承：oprning a new branch in ',addr)

class Teacher(SchoolMember,School):     # 多继承：Teacher子类继承了SchoolMember、School两个父类
    '''教师子类'''
    def __init__(self,name,age,sex,salary,course):
        SchoolMember.__init__(self,name,age,sex)       #经典类写法
        #super(Teacher,self).__init__(name,age,sex)    #新式类写法
        self.salary = salary
        self.course = course


    def teaching(self):
        print("Teacher [%s] is teaching 【%s】" %(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,course,tuition):
        SchoolMember.__init__(self,name,age,sex)
        self.course = course
        self.tuition= tuition
        self.amount = 0

    def pay_tuition(self,amount):
        print('Student [%s] has just paied 【%s】'%(self.name,amount))
        self.amount += amount

t1 = Teacher('wusir',28,'女',3000,'Python')
s1 = Student('HaiTao',38,'N/A','PYS152',15000)
s2 = Student('LiChuang',12,'M','Java',11000)


print(SchoolMember.member)  #打印原始 SchoolMember.member 已注册人数
del s2                      #使用析构方法  删除s2实例
print(SchoolMember.member)  #打印析构后 已注册人数

t1.tell()                   #打印t1的详细信息
s1.tell()

t1.oprn_branch('ShangHai')     #t1这个实例可以SchoolMember、School两个类中的方法