from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from cmdb import models
from django.views import View
# Create your views here.
def login(request):
    '''
    用户登录接口
    :param request:
    :return:
    '''
    mesg = ""
    if request.method == "POST":
        user = request.POST.get("user.txt",None)
        password = request.POST.get("password",None)
        print(user,password)
        result = models.User_admin.objects.filter(user_name = user,password=password).first()
        if result:
            return redirect('/cmdb/home')
        else:
            mesg = "用户名和密码不匹配"
    return render(request,'登录.html',{"error_mesg":mesg})


def home(request):
    '''
    后台管理接口
    :param request:
    :return:
    '''
    return render(request,'后台管理.html')

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
        obj = models.User_admin.objects.all()
        return render(request, "user_info.html",{"obj":obj})

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

class User_Insert(View):
    '''
    添加用户接口
    '''
    def dispatch(self, request, *args, **kwargs):
        result = super(User_Insert,self).dispatch(request,*args,**kwargs)
        return result

    def post(self,request):
        user = request.POST.get("username", None)
        pwd = request.POST.get("pwd", None)
        email = request.POST.get("email", None)
        model = request.POST.get("model", None)
        type = request.POST.get("type", None)
        group = request.POST.get("group", None)
        print(user, pwd, email, model, type, group)
        models.User_admin.objects.create(user_name=user,password=pwd,email=email,model=model,type=type,user_group_id=group)
        return redirect('/cmdb/user_insert')

    def get(self,request):
        obj = models.User_admin.objects.all()
        return render(request, "user_insert.html", {"obj": obj})


def rom(request):
    # models.User_Group.objects.create(group_name="CEO",shop_id=1002)
    # models.User_admin.objects.create(user_name="alex",password = "admin",email='alex@163.com')
    # models.User_admin.objects.create(user_name="kyo", password="admin1")
    # models.User_admin.objects.create(user_name="Mary", password="root")
    # models.User_admin.objects.create(user_name="admin-2", password="admin2")
    # models.User_admin.objects.create(user_name="j-product", password="product")
    # models.User_Group.objects.create(group_name="QA",shop_id=1002)
    return HttpResponse("Rom")