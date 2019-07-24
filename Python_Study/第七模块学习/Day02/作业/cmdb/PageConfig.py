# -*- coding:utf-8 -*-
# Author:D.Gray
from django.utils.safestring import mark_safe
class PageConfig(object):
    def __init__(self,current_page,totle,per_page,jump_page,page_num=7):
        '''

        :param current_page: 当前页
        :param totle_page: 总页数
        :param per_page: 一页显示X个
        :param page_num: 一行多少页数
        :param jump_page: 跳转到X页
        '''
        self.current_page = current_page
        self.totle = totle
        self.per_page = per_page
        self.jump_page = jump_page
        self.page_num = page_num
    @property
    def start(self):
        return (self.current_page-1)*self.per_page

    @property
    def end(self):
        return self.current_page*self.per_page

    @property
    def totle_count(self):
        count,y = divmod(self.totle,self.per_page)
        if y:
            count += 1
        return count

    def per_str(self):
        page_list = []
        if self.totle_count <= self.page_num:
            start_index = 1
            end_index = self.totle_count + 1
        else:
            if self.current_page <= (self.page_num + 1)/2:
                start_index = 1
                end_index = self.page_num + 1
            else:
                start_index = self.current_page - (self.page_num - 1)/2
                end_index = self.current_page + (self.page_num + 1)/2
            if self.current_page + (self.page_num - 1)/2 > self.totle_count:
                start_index = self.totle_count - (self.page_num - 1)/2
                end_index = self.totle_count + 1
        if self.current_page == 1:
            pass
        else:
            affter = "<button class='pageX'><a href='/cmdb/user_info/?p=%s'>上一页</a></button>"%(self.current_page-1)
            first = "<button class='pageX'><a href='/cmdb/user_info/?p=1'>首页</a></button>"
            page_list.append(affter)
            page_list.append(first)
        for row in range(int(start_index),int(end_index)):
            if row == self.current_page:
                tmp = "<button class='page active'>%s</button>"%(row)
            else:
                tmp = "<button class='page'>%s</button>" % (row)
            page_list.append(tmp)
        if self.current_page == self.totle_count:
            pass
        else:
            next = "<button class='pageX'><a href='/cmdb/user_info/?p=%s'>下一页</a></button>"%(self.current_page+1)
            end = "<button class='pageX'><a href='/cmdb/user_info/?p=%s'>尾页</a></button>"%(self.totle_count)
            page_list.append(end)
            page_list.append(next)
        page_str = "".join(page_list)
        page_str = mark_safe(page_str)
        return page_str
