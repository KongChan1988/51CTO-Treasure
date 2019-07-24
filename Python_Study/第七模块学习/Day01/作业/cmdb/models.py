from django.db import models
# Create your models here.
class User_admin(models.Model):
    '''
    user_admin表数据操作
    '''
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    model = models.IntegerField(null=True)
    type_choices = (
        (1,"黄金VIP用户"),
        (2, "VIP用户"),
        (3, "普通用户"),
    )
    type = models.IntegerField(choices=type_choices,default=3)
    user_group = models.ForeignKey('User_Group',to_field="group_id",on_delete=models.CASCADE,default=1)  #外键关联user_group表
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class User_Group(models.Model):
    '''
    user_group表数据操作
    '''
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=64)
    shop_id = models.IntegerField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

