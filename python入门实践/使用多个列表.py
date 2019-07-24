#比萨店配料列表
available_toppings=['mushrooms','olives','green peppers',
                    'pepperoni','pineapple','extra cheese']
#顾客配料列表
requested_toppings=['mushrooms','french fries','extra cheese','green peppers']


#任务一：将顾客配料列表与比萨店配料列表做对比
#如果顾客配料列表中元素包含在比萨店配料列表中，给出可以添加配料
#反之则给出“没有该配料的提示”
for requested_topping in requested_toppings: #定义变量requested_topping遍历
	                                         #整个顾客配料列表
    if requested_topping in available_toppings: #如果变量requested_topping的元素
		                                        #包含在比萨店配料列表中，返回值为
		                                        #True并打印print语句
        print('Adding '+requested_topping+'.')
    else:
        print("Sorry,we don't hava "+requested_topping+'.')
print("\nFinished making your pizza!")
    


#任务二：在任务一基础上
#1）添加顾客配料列表为空时，给出“是否确实要点普通比萨”判断
#2）当顾客配料列表中有‘green peppers’时，给出“对不起该配料今天已售完”判断

#比萨店配料列表
available_toppings=['mushrooms','olives','green peppers',
                    'pepperoni','pineapple','extra cheese']
#顾客配料列表
requested_toppings=['green peppers','mushrooms','french fries','extra cheese']
print('\n任务二：')
if requested_toppings:#首先判断顾客配料列表是否为空
	                  #若列表有数值，返回值为True执行for循环
	                  #若列表无数值，返回值为False执行else语句
	for requested_topping in requested_toppings:#执行for循环遍历		                                        
		print(requested_topping)                #requested_topping列表
		if requested_topping =='green peppers':#最初判断变量是否等于'green peppers'
			print('对不起该配料(青椒)今天已售完')   #返回值False时，跳过print语句
			                                   #执行elif语句
		elif requested_topping in available_toppings:#如果变量元素在比萨店配料列表中
			print('Adding '+requested_topping+'.')#返回值为True并执行“Adding”语句
		else:
			print("Sorry,we don't hava "+requested_topping+'.')#反之则执行“Sorry”
else:
	print("是否确实要点普通比萨")
print("\nFinished making your pizza!")





























