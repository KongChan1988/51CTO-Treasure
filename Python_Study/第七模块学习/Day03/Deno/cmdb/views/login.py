# -*- coding:utf-8 -*-
# Author:D.Gray
from django.shortcuts import render,HttpResponse,redirect
from cmdb import formes
from cmdb import models
import json,os
def login(request):
    if request.method == "GET":
        obj = formes.UserInfoModelForm()
        return render(request,"Model_forms_login.html",{"obj":obj})
    elif request.method =="POST":
        obj = formes.UserInfoModelForm(request.POST,request.FILES)
        r1 = obj.is_valid()
        if r1:
            # obj.save()
            instance = obj.save(False)    #自定义obj.save()
            instance.save()     #只保存到当前表操作 不保存到m2m表
            # obj.save_m2m()
            print("验证成功:",obj.cleaned_data)
            return HttpResponse("验证成功")
        else:
            print("验证失败:",obj.errors)
            return render(request,"Model_forms_login.html",{"obj":obj})
    return render(request,"Model_forms_login.html")

from django.core.exceptions import ValidationError
import json
class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field, ValidationError):
            return {"code":field.code,"message":field.message}
        else:
            return json.JSONEncoder.default(self, field)

def login_ajax(request):
    res = {"status":True,"error":None,"data":None}
    if request.method == "GET":
        obj = formes.Login_ajax()
        return render(request,"login_ajax.html",{"obj":obj})
    elif request.method =="POST":
        obj = formes.Login_ajax(request.POST,request.FILES)
        r1 = obj.is_valid()
        if r1:
            print("验证成功:",obj.cleaned_data)
        else:
            print("验证失败:",obj.errors)
            res["error"] = obj.errors.as_data()
        result = json.dumps(res,cls=JsonCustomEncoder)
        return HttpResponse(result)


def Register(request):
    if request.method == "GET":
        obj = formes.RegisterProm()
        return render(request,"register.html",{"obj":obj})
    elif request.method =="POST":
        obj = formes.RegisterProm(request.POST,request.FILES)
        r1 = obj.is_valid()
        if r1:
            print("验证成功:",obj.cleaned_data)
            return HttpResponse("验证成功")
        else:
            print("验证失败:",obj.errors)
            return render(request,"register.html",{"obj":obj})
    return render(request,"register.html")


def user_list(request):
    li = models.UserInfo.objects.all().select_related("user_type")
    return render(request,"user_list.html",{"li":li})

def user_edit(request,nid):
   if request.method == "GET":
       user_obj = models.UserInfo.objects.filter(id=nid).first()
       mf = formes.UserInfoModelForm(instance=user_obj)
       return render(request,"user_edit.html",{"mf":mf,"nid":nid})
   elif request.method == "POST":
       user_obj = models.UserInfo.objects.filter(id=nid).first()
       mf = formes.UserInfoModelForm(request.POST,instance=user_obj)
       if mf.is_valid():
           mf.save()
       else:
           print(mf.errors.is_json())
       return render(request, "user_edit.html", {"mf": mf, "nid": nid})

def upload(request):
    return render(request,"upload.html")

def upload_file(request):
    res = {"status":True,"data":request.POST}
    username = request.POST.get("root",None)
    file = request.FILES.get("file",None)
    print(username,file)
    file_path = os.path.join("E:\\python_work\\51CTO_Python\第七模块学习\Day03\Deno\cmdb\\upload",file.name)
    with open(file_path,"wb") as f:
        for item in file.chunks():
            f.write(item)
    return HttpResponse(json.dumps(res))

