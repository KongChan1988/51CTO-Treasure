#输入一个年份，判断是否是闰年
while True:
    year = input('请输入一个年份>>>: ')
    if year.isdigit():
        year = int(year)
        if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
            print('是闰年')
        else:
            print("不是闰年")
    else:
        print("请输入有效年份")
