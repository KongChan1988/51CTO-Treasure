from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from cmdb import models
from django.views import View
from django.utils.decorators import method_decorator
from cmdb.PageConfig import PageConfig
import json
# Create your views here.
def auth(func):
    def inner(request,*args,**kwargs):
        v = request.COOKIES.get("ASP.NET_SessionId")
        if not v:
            return redirect("/cmdb/login")
        return func(request,*args,**kwargs)
    return inner

def login(request):
    '''
    用户登录接口
    :param request:
    :return:
    '''
    mesg = ""
    if request.method == "POST":
        user = request.POST.get("user",None)
        password = request.POST.get("password",None)
        # print(user,password)
        result = models.User_admin.objects.filter(user_name = user,password=password).first()
        if result:
            res = redirect('/cmdb/home')
            res.set_signed_cookie("ASP.NET_SessionId","",salt=password)
            return res
        else:
            mesg = "用户名和密码不匹配"
    return render(request,'登录.html',{"error_mesg":mesg})

@auth
def home(request):
    '''
    后台管理接口
    :param request:
    :return:
    '''
    return render(request,'后台管理.html')

@auth
def user_info(request):
    '''
    用户管理接口
    :param request:
    :return:
    '''
    if request.method == "POST":
        text = request.POST.get("text",None)
        if str(text).isdigit():    #判断text内容是否为整数， 如果是整数就用户ID搜索，如果是字符串就用户名搜索
            text = int(text)
            obj = models.User_admin.objects.filter(user_id=text).all()
            return render(request, "user_info.html", {"obj": obj})
        else:
            obj = models.User_admin.objects.filter(user_name__icontains=text).all()
            return render(request, "user_info.html",{"obj":obj})
    else:
        current_page = request.GET.get("p",1)
        current_page = int(current_page)
        obj = models.User_admin.objects.all()
        page_obj = PageConfig(current_page=current_page,per_page=5,totle=len(obj),jump_page=1)
        data = obj[page_obj.start:page_obj.end]
        page_obj.per_str()
        return render(request, "user_info.html",{"obj":data,"per_str":page_obj.per_str(),"total":page_obj.totle_count})

@auth
def user_detail(request,nid):
    '''
    用户详情管理接口
    包括用户信息编辑
    :param request:
    :param nid:
    :return:
    '''
    if request.method == "POST":
        user = request.POST.get("username",None)
        pwd = request.POST.get("pwd",None)
        email = request.POST.get("email", None)
        model = request.POST.get("model", None)
        type = request.POST.get("type", None)
        group = request.POST.get("group", None)
        print(user,pwd,email,model,type,group)

        models.User_admin.objects.filter(user_id=nid).update(user_name=user,
                                                                   password=pwd,email=email,model=model,
                                                                   type=type,user_group_id=group)
        return redirect('/cmdb/user_info-%s'%nid)
    else:
        row = models.User_admin.objects.filter(user_id=nid).first()
        return render(request, "user_detail.html",{"row": row})

@method_decorator(auth,name="dispatch")
class User_Delete(View):
    '''
    删除用户接口
    '''
    def dispatch(self, request, *args, **kwargs):
        result = super(User_Delete,self).dispatch(request,*args,**kwargs)
        return result

    def post(self,request,nid):
        models.User_admin.objects.filter(user_id=self.kwargs['nid']).delete()
        return redirect('/cmdb/user_info')

    def get(self,request,nid):
        models.User_admin.objects.filter(user_id=self.kwargs['nid']).delete()
        return redirect('/cmdb/user_info')

@method_decorator(auth,name="dispatch")
class User_Insert(View):
    '''
    添加用户接口
    '''
    def dispatch(self, request, *args, **kwargs):
        result = super(User_Insert,self).dispatch(request,*args,**kwargs)
        return result

    def post(self,request):
        res = {"status":True,"error":None,"data":None}
        try:
            user = request.POST.get("username", None)
            pwd = request.POST.get("pwd", None)
            email = request.POST.get("email", None)
            model = request.POST.get("model", None)
            type = request.POST.get("type", None)
            group = request.POST.get("group", None)
            print(user, pwd, email, model, type, group)
            models.User_admin.objects.create(user_name=user,password=pwd,email=email,model=model,type=type,user_group_id=group)
            return redirect('/cmdb/user_insert')
        except Exception as f:
            res["status"] = False
            res["error"] = "数据异常:%s"%(f)
        return HttpResponse(json.dumps(res))

    def get(self,request):
        obj = models.User_admin.objects.all()
        return render(request, "user_insert.html", {"obj": obj})


def rom(request):
    for i in range(51):
        # models.User_Group.objects.create(group_name="CEO",shop_id=1002)
        # models.User_admin.objects.create(user_name="alex",password = "admin",email='alex@163.com')
        # models.User_admin.objects.create(user_name="kyo", password="admin1")
        # models.User_admin.objects.create(user_name="Mary", password="root")
        models.User_admin.objects.create(user_name="admin-%s"%i, password="admin2")
        # models.User_admin.objects.create(user_name="j-product", password="product")
        # models.User_Group.objects.create(group_name="QA",shop_id=1002)
    return HttpResponse("Rom")