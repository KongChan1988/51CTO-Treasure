from django.shortcuts import render
from django import forms
# Create your views here.
class FM(forms.Form):
    user = forms.CharField(error_messages={"required":"用户名不能为空"})
    pwd = forms.CharField(
        max_length=12,
        min_length=6,

    )
    email = forms.EmailField()

def login(request):
    if request.method == "GET":
        obj = FM()
        return render(request,"forms.html",{"obj":obj})
    elif request.method == "POST":
        obj = FM(request.POST)
        r1 = obj.is_valid()
        if r1:
            print(obj.cleaned_data)
        else:
            return render(request,"forms.html")
    return render(request,"forms.html")