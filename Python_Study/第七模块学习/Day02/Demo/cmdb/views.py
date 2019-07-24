from django.shortcuts import render
from django.utils.safestring import mark_safe
from utils.Pagemation import PageMation

# Create your views here.
def tp1(request):
    page = request.GET.get("p",1)
    page = int(page)
    list = []
    for i in range(1,101):
        list.append(i)
    start = (page-1)*10
    end = page*10
    data = list[start:end]
    all_page = len(list)
    count,y = divmod(all_page,10)
    if y:
        count += 1
    count_list = []
    for item in range(1,count+1):
        if item == page:
            tmp = "<a class = 'page active' href = '/tp1/?p=%s'>%s</a>"%(item,item)  #点击当前页后触发active属性
        else:
            tmp = "<a class = 'page' href = '/tp1/?p=%s'>%s</a>" % (item, item)
        count_list.append(tmp)
    page_str = "".join(count_list)
    page_str = mark_safe(page_str)
    return render(request,"tp1.html",{"list":data,"page_str":page_str})

def tp2(request):
    list = []
    for i in range(1,101):
        list.append(i)
    return render(request,"tp2.html",{"list":list})

def tp3(request):
    current_page = request.GET.get("p",1)
    current_page = int(current_page)
    list = []
    for i in range(1,501):
        list.append(i)
    totle_page = len(list)
    page_obj = PageMation(current_page=current_page,all_page=totle_page)
    data = list[page_obj.start:page_obj.end]
    page_obj.page_str()


    # data = list[(current_page-1)*pre_page:current_page*pre_page]
    # count,v = divmod(totle_page,pre_page)
    # if v:
    #     count +=1
    # page_list = []
    # if count < page_num:
    #     start_index = 1
    #     end_index = count + 1
    # else:
    #     if current_page <= (page_num - 1)/2:
    #         start_index = 1
    #         end_index = page_num + 1
    #     else:
    #         start_index = current_page - (page_num-1)/2
    #         end_index = current_page + (page_num+1)/2
    #     if current_page + (page_num-1)/2 > count:
    #         start_index = current_page - (page_num-1)/2
    #         end_index = count + 1
    # for row in range(int(start_index),int(end_index)):
    #     print(row)
    #     if row == current_page:
    #         tmp = "<a class='page active' href='/tp3/?p=%s'>%s</a>"%(row,row)
    #     else:
    #         tmp = "<a class='page' href='/tp3/?p=%s'>%s</a>" % (row, row)
    #     page_list.append(tmp)
    # page_str = "".join(page_list)
    # page_str = mark_safe(page_str)
    return render(request,"tp3.html",{"list":data,"page_str":page_obj.page_str()})

#

