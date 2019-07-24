from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.shortcuts import render
def login(request):
    mesg = ""
    if request.method == "POST":
        user = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print(user,password)
        if user == "root" and password == "admin":
            return redirect("/home")
        else:
            mesg = "用户名和密码不匹配"
    return render(request,"login.html",{"error_mesg":mesg})
USER_LIST = [
    {"username":"alex","sex":"男","email":"alex@163.com"}
]
def home(request):
    if request.method == "POST":
        user = request.POST.get('username',None)
        sex = request.POST.get("sex",None)
        email = request.POST.get("email", None)
        tmp = {"username":user,"sex":sex,"email":email}
        USER_LIST.append(tmp)
    return render(request,"home.html",{"user_list":USER_LIST})