#方法一
aliquot=[num for num in range(3,31,3)]
print(aliquot)

#方法二
aliquot=[]
for i in range(3,31):
	if i%3==0:
		aliquot.append(i)
		#print(i)
print(aliquot)
