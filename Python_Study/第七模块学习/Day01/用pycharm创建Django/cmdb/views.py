from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
USER_DICT = {
    "1":{"name":"root1","email":"root1@163.com"},
    "2":{"name":"root2","email":"root2@163.com"},
    "3":{"name":"root3","email":"root3@163.com"},
    "4":{"name":"root4","email":"root4@163.com"},
    "5":{"name":"root5","email":"root5@163.com"},
}
def index(request):
    return render(request,"index.html",{"user_dict":USER_DICT})

def detail(request):
    nid = request.GET.get("nid")
    detail_info = USER_DICT[nid]
    return render(request,"detail.html",{"detail_info":detail_info})

def detail_z(request,*args,**kwargs):
    print(args)
    detail_info = USER_DICT[args[0]]
    return render(request, "detail.html", {"detail_info": detail_info})

def detail_x(request,*args,**kwargs):
    print(kwargs)
    detail_info = USER_DICT[kwargs["nid"]]
    return render(request, "detail.html", {"detail_info": detail_info})
