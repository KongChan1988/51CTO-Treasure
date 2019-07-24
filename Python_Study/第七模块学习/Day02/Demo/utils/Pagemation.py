# -*- coding:utf-8 -*-
# Author:D.Gray
from django.utils.safestring import mark_safe
class PageMation(object):
    '''
    定义一个分页类
    current_page = 当前页
    all_page = 所有数据个数
    per_page = 每页显示X条数据
    page_num = 一行分X页
    '''
    def __init__(self,current_page,all_page,per_page=10,page_num=7):
        self.current_page = current_page
        self.all_page = all_page
        self.per_page = per_page
        self.page_num = page_num

    @property
    def start(self):
        return (self.current_page-1) * self.per_page

    @property
    def end(self):
        return self.current_page * self.per_page

    @property
    def totle_page(self):
        count,v = divmod(self.all_page,self.per_page)
        if v:
            count += 1
        return count

    def page_str(self):
        page_list = []
        if self.totle_page < self.page_num:    #总页数小于最大分页数
            start_index = 1
            end_index = self.page_num
        else:
            if self.current_page <= (self.page_num - 1)/2:      #当前页小于等于页数分割值
                start_index = 1
                end_index = self.page_num + 1
            else:
                start_index = self.current_page - (self.page_num - 1 )/2
                end_index = self.current_page + (self.page_num + 1)/2
            if self.current_page + (self.page_num - 1)/2 > self.totle_page:  #当前页大于最大页数
                start_index = self.current_page - (self.page_num-1)/2
                end_index = self.totle_page + 1
        if self.current_page == 1:
            pass
        else:
            perv = "<a class='page' href='/tp3/?p=%s'>上一页</a>"%(self.current_page-1)
            first = "<a class='page' href='/tp3/?p=1'>首页</a>"
            page_list.append(perv)
            page_list.append(first)
        for row in range(int(start_index),int(end_index)):
            if row == self.current_page:
                tmp = "<a class='page active' href='/tp3/?p=%s'>%s</a>"%(row,row)
            else:
                tmp = "<a class='page' href='/tp3/?p=%s'>%s</a>" % ( row, row)
            page_list.append(tmp)
        if self.current_page == self.totle_page:
            pass
        else:
            next = "<a class='page' href='/tp3/?p=%s'>下一页</a>" % (self.current_page + 1)
            last = "<a class='page' href='/tp3/?p=%s'>尾页</a>"%(self.totle_page)
            page_list.append(last)
            page_list.append(next)

        page_str = "".join(page_list)
        page_str = mark_safe(page_str)
        return page_str