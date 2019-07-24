from django.shortcuts import render,redirect,HttpResponse
from app02 import models

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":
        user = request.POST.get("username",None)
        pwd = request.POST.get("password",None)
        rmb = request.POST.get("rmb",None)
        if user == "root" and pwd == "123":
            request.session["username"] = user
            request.session["is_login"] = True
            if rmb == "1":
                request.session.set_expiry(10)
            return redirect("/app02/index/")
        else:
            return render(request, "login.html")

def index(request):
    if request.session.get("is_login",None):
        return render(request,"index.html")
    else:
        return HttpResponse("滚")

def logout(request):
    request.session.clear()
    return redirect("/app02/login/")

def test(request):
    print("小姨妈---付钱啦")
    return HttpResponse("OK")

from django.views.decorators.cache import cache_page
# @cache_page(10)     #定义views函数全局缓存
def cache(request):
    import time
    ctime = time.time()
    return render(request,"cache.html",{"ctime":ctime})

def sigin(request):
    obj = models.UserInfo(user="root")
    print("end")
    obj.save()

    from sg import pizza_done
    pizza_done.send(sender="sdsdsd",topping=123,size=456)
    return HttpResponse("ok")