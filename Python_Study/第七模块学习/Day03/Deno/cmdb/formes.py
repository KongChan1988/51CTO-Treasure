# -*- coding:utf-8 -*-
# Author:D.Gray
from django import forms
from django.forms import widgets,fields as Fields
from django.forms import ModelForm
from cmdb import models
class UserInfoModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = "__all__"
        # fields = ["name","pwd","email"]
        labels = {
            "name":"用户名",
            "pwd":"密码"
        }
        help_texts = {
            "pwd":"最小长度6位"
        }
        widgets = {
            "pwd":widgets.PasswordInput(attrs={"placeholder":"请输入密码"})
        }
        error_messages = {
            "__all__":{
                "ValidationError":"用户名或密码错误"
            },
            "email":{
                "required":"邮箱不能为空",
                "invalid":"邮箱格式错误"
            }
        }

class UserInfoForms(forms.Form):
    user = Fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={"placeholder":"请输入用户名"})
    )
    pwd = Fields.CharField(
        max_length=12,min_length=6,
        widget = widgets.PasswordInput(attrs={"placeholder": "请输入密码"})
    )
    email = Fields.EmailField(
        widget=widgets.TextInput(attrs={"placeholder": "请输入邮箱"}),
        error_messages={"required":"邮箱不能为空","invalid":"邮箱格式不对"}
    )

    user_type = Fields.ChoiceField(
        choices=[]
    )
    from django.forms.models import ModelChoiceField
    user_type2 = ModelChoiceField(
        to_field_name="id",
        empty_label="请选择用户类型",
        queryset=models.UserType.objects.all()
    )
    def __init__(self,*args,**kwargs):
        super(UserInfoForms,self).__init__(*args,**kwargs)
        self.Fields["user_type"].choices = models.UserType.objects.values_list("id","name")

from django.core.exceptions import ValidationError
class RegisterProm(forms.Form):
    '''
    定义一个注册form验证
    '''
    user = Fields.CharField(
        widget=widgets.TextInput(attrs={"placeholder": "请输入用户名"})
    )
    pwd = Fields.CharField(
        max_length=12, min_length=6,
        widget=widgets.PasswordInput(attrs={"placeholder": "请输入密码"})
    )
    email = Fields.EmailField(
        widget=widgets.TextInput(attrs={"placeholder": "请输入邮箱"}),
        error_messages={"required": "邮箱不能为空", "invalid": "邮箱格式不对"}
    )
    def clean_user(self):
        c = models.UserInfo.objects.filter(name=self.cleaned_data["user"]).count()
        if not c:
            return self.cleaned_data["user"]
        else:
            raise ValidationError("用户名已存在",code="11223")

    def clean_email(self):
        return self.cleaned_data["email"]

    def clean(self):
        #对整体进行验证  用户名或密码错误 在这里提示
        c = models.UserInfo.objects.filter(name=self.cleaned_data["user"],pwd=self.cleaned_data["pwd"]).count()
        if c:
            return self.cleaned_data
        else:
            raise ValidationError("用户名或密码错误")
    def _post_clean(self):
        '''
        自定义验证函数
        :return:
        '''
        pass

class Login_ajax(forms.Form):
    user = Fields.CharField(
        required=True,
        widget=widgets.TextInput(attrs={"placeholder": "请输入用户名"})
    )
    pwd = Fields.CharField(
        max_length=12, min_length=6,
        widget=widgets.PasswordInput(attrs={"placeholder": "请输入密码"})
    )
    email = Fields.EmailField(
        widget=widgets.TextInput(attrs={"placeholder": "请输入邮箱"}),
        error_messages={"required": "邮箱不能为空", "invalid": "邮箱格式不对"}
    )
    def clean(self):
        #对整体进行验证  用户名或密码错误 在这里提示
        c = models.UserInfo.objects.filter(name=self.cleaned_data["user"],pwd=self.cleaned_data["pwd"]).count()
        if c:
            return self.cleaned_data
        else:
            raise ValidationError("用户名或密码错误")