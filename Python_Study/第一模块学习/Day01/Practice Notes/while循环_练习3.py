#-*- Coding:utf-8 -*-
# Author: D.Gray
'''
梦想的度假圣地：编写一个程序，调查用户梦想的度假圣地。使用类似于"If you could visit one place in the
world,where would you go?"的提示，并编写一个打印调查结果的代码快
'''
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat's you name? ")
    response = input("If you could visit one place in the world,where would you go?")

    if (name == '' or response == '') or (name ==  ' ' or response ==  ' '):
        print('User information cannot be empty ')

    else:
        responses[name] = response  # responses{name:response}将用户输入
                                    # 的name和response存储到responses字典中
        repeat = input('Would you like to let another person respond?(yes/no)')#询问用户是否继续参与调查
        if repeat == 'no':
            break

        print('\n---Poll Results---')
        for name,response in responses.items(): #循环遍历responses字典中的键值对参数
            print(name.title(),'would like to go',response,'.')