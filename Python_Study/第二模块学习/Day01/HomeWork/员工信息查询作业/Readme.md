一、作业需求：

(1).工信息表程序，实现增删改查操作：

(2).可进行模糊查询，语法至少支持下面3种:
   
	select name,age from staff_table where age > 22
   	select * from staff_table where dept = "IT"
   	select * from staff_table where enroll_date like "2013"
(3).查到的信息，打印后，最后面还要显示查到的条数

(4).可创建新员工纪录，以phone做唯一键，staff_id需自增

(5).可删除指定员工信息纪录，输入员工id，即可删除

(6).可修改员工信息，语法如下:
 
	UPDATE staff_table SET dept = "Market" where dept = "IT"
 注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码


二、博客地址：http://www.cnblogs.com/catepython/p/7551288.html

三、程序目录结构：

|——员工信息查询系统
|——bin目录
|	|—— _init.py
|	|__	Stary.py
|
|——core目录
|	|——	__init__.py
|	|——	main.py
|	|——	parses.py
|	|__	action.py
|
|——db目录
|	|——	emp
|	|__	xmp
|
|__  __init.py__

四、运行环境

操作系统：Win10

Python：3.6.2rcl

Pycharm：2017.1.14

五、功能实现

1）实现了基本需求，如用户输入操作序号能进入相应的操作环境

2）在指定操作环境下只能输入相应的关键字 如：在查询模块中只能输入select关键字，添加模块中只能输入insert关键字

3）查询出相应结果后会给出查询结果数量统计

4）能根据用户输入的sql语句执行并给出相应结果

5）以多函数形式避免了代码不必要的重复

六、测试

1）开始程序后在选择操作模块时，实现了为空无效超范围判断

2）在各模块中输入无效字符或非select关键字，给出‘sql关键字无效’
判断

3）输入正确有效select语句能查询出相应结果和给出查询数量

4）输入有效update语句能给出修改完成或错误提示，修改完成db数据库文件文本内容也同步修改

5）输入有效delect语句能删除数据库中相应文本内容

6）输入有效insert语句能增加员工信息记录，并完成id自增和手机号唯一判断

七、备注

